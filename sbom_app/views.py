from django.shortcuts import render, redirect
from django.views import View
from .models import UploadedFile, SbomAppSbomData, SearcheData, SbomVulData, CveData, LicenseMaster
from django.http import HttpResponse
from .parsing import SPDX, SPDX_JSON, cyDX_JSON
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import json
import csv
from django.conf import settings
import os
import ast

#Upload SBOM
class FileUploadView(View):
    def get(self, request):
        file_id = request.session.get('file_id')

        try:
            dashboard_name = SbomAppSbomData.objects.filter(file_id=file_id).first()
            dashboard_name = dashboard_name.name.split()[0]
        except:
            pass

        sbom_vul_data = SbomVulData.objects.filter(file_id=file_id)
        package_count = SbomAppSbomData.objects.filter(file_id=file_id).count()
        vul_count = SbomVulData.objects.filter(file_id=file_id).count()
        package_statistics = package_count-vul_count
        license = SbomAppSbomData.objects.filter(file_id=file_id).first()
        risk_low = SbomVulData.objects.filter(file_id=file_id,risklevel='LOW').count()
        risk_medium = SbomVulData.objects.filter(file_id=file_id,risklevel='MEDIUM').count()
        risk_high = SbomVulData.objects.filter(file_id=file_id,risklevel='HIGH').count()
        risk_critical = SbomVulData.objects.filter(file_id=file_id,risklevel='CRITICAL').count()
        
        if license:
            license_info = license.license_info
            license_info_list = license_info.strip("[]").split(", ")
            license_count = len(license_info_list)
        else:
            license_count = 0

        return render(request, 'index.html', {'sbom_vul_data': sbom_vul_data, 'package_count': package_count, 'vul_count': vul_count, 'license_count': license_count,
                                              'package_statistics': package_statistics, 'risk_low': risk_low, 'risk_medium': risk_medium, 'risk_high': risk_high, 'risk_critical':risk_critical, 'dashboard_name':dashboard_name})
    
    # upload POST
    def post(self, request):
        uploaded_file = request.FILES.get('file')
        
        if uploaded_file:
            file_instance = UploadedFile(file=uploaded_file)
            file_instance.save()
            file_path = file_instance.file.path
            request.session['file_id'] = file_instance.id
            name, version, license_info, license, originator, md5_hash, sha1_hash, sha256_hash = self.parse_uploaded_file(file_path)

            for i in range(0,len(name)):
                sbom_data_instance = SbomAppSbomData()
                sbom_data_instance.file_id = file_instance.id
                sbom_data_instance.version = version[i]
                sbom_data_instance.name = name[i]
                sbom_data_instance.license_info = license_info
                sbom_data_instance.license = license[i]
                sbom_data_instance.originator = originator[i]
                sbom_data_instance.md5_hash = md5_hash[i]
                sbom_data_instance.sha1_hash = sha1_hash[i]
                sbom_data_instance.sha256_hash = sha256_hash[i]
                sbom_data_instance.save()
        
            search_results = self.search_data(name, version)
            search_results_json = json.dumps(search_results, indent=4)
            search_results_list = json.loads(search_results_json)
            
            for i in range(len(search_results_list)):
                sbom_vul_data = SbomVulData()
                sbom_vul_data.file_id = file_instance.id
                sbom_vul_data.cve = search_results_list[i]['cve_id']
                sbom_vul_data.product = search_results_list[i]['product']
                sbom_vul_data.version = search_results_list[i]['version']
                sbom_vul_data.save()
            
                cve_data = CveData.objects.get(cve_id=search_results_list[i]['cve_id'])
                data_string = cve_data.data
                data_json = json.loads(data_string)
                
                try:
                    description_value = data_json['cve']['description']['description_data'][0]['value']
                except (KeyError, IndexError):
                    description_value = 'No Description'
                    
                try:
                    risk_score = data_json['impact']['baseMetricV3']['cvssV3']['baseScore']
                except (KeyError, IndexError):
                    risk_score = 'No Risk Score'
                
                try:
                    risk_level = data_json['impact']['baseMetricV3']['cvssV3']['baseSeverity']
                except (KeyError, IndexError):
                    risk_level = 'No Risk Level'

                try:
                    cwe_id = data_json['cve']['problemtype']['problemtype_data'][0]['description'][0]['value']
                except (KeyError, IndexError):
                    cwe_id = 'No CWE ID'
                    
                sbom_vul_data.description = description_value
                sbom_vul_data.riskscore = risk_score
                sbom_vul_data.risklevel = risk_level
                sbom_vul_data.cwe = cwe_id
                sbom_vul_data.save()

            os.remove(file_path)
            
            return redirect('index')
        else:
            return redirect('index')
        

    #
    def parse_uploaded_file(self, file_path):
        name = None
        version = None
        license_info = None
        license = None
        md5_hash = None
        sha1_hash = None
        sha256_hash = None
        originator = None

        try:
            name, version, license_info, license, originator, md5_hash, sha1_hash, sha256_hash = cyDX_JSON(file_path)
        except Exception as e:
            pass

        if name is None or version is None:
            try:
                name, version, license_info, license, originator, md5_hash, sha1_hash, sha256_hash = SPDX_JSON(file_path)
            except Exception as e:
                pass

        if name is None or version is None:
            name, version, license_info, license, originator, md5_hash, sha1_hash, sha256_hash = SPDX(file_path)
        
        return name, version, license_info, license, originator, md5_hash, sha1_hash, sha256_hash
    
    def search_data(self, name, version):
        search_results = []
        
        for name,version in zip(name,version):
            result = SearcheData.objects.filter(Q(product=name) & Q(version=version)).values('product', 'version', 'cve_id')
            search_results.extend(result)
        
        return search_results


#SBOM list
def sbomlist(request):
    file_id = request.session.get('file_id')
    items_per_page = settings.PAGINATOR_ITEMS_PER_PAGE
    entries = SbomAppSbomData.objects.filter(file_id=file_id).order_by('name')
    paginator = Paginator(entries, items_per_page)
    vul_count = SbomVulData.objects.filter(file_id=file_id).count()
    page = request.GET.get('page')
    
    try:
        page_items = paginator.get_page(page)
    except PageNotAnInteger:
        page_items = paginator.get_page(1)
    except EmptyPage:
        page_items = paginator.get_page(paginator.num_pages)

    return render(request, 'sbomlist.html', {'page_items': page_items, 'vul_count': vul_count})

#Vul List
def vullist(request):
    file_id = request.session.get('file_id')
    items_per_page = settings.PAGINATOR_ITEMS_PER_PAGE
    entries = SbomVulData.objects.filter(file_id=file_id).order_by('cve')
    paginator = Paginator(entries, items_per_page)
    vul_count = SbomVulData.objects.filter(file_id=file_id).count()
    page = request.GET.get('page')
    
    try:
        page_items = paginator.get_page(page)
    except PageNotAnInteger:
        page_items = paginator.get_page(1)
    except EmptyPage:
        page_items = paginator.get_page(paginator.num_pages)
        
    return render(request, 'vullist.html', {'page_items': page_items, 'vul_count': vul_count})

#Lic List
def liclist(request):
    file_id = request.session.get('file_id')
    license_infos = SbomAppSbomData.objects.filter(file_id=file_id).values('license_info').first()

    # Ensure license_infos is not None before accessing 'license_info'
    if license_infos:
        license_info_str = license_infos.get('license_info', '[]')
        license_info = ast.literal_eval(license_info_str)

        license_objects = []

        # Iterate through license_info array
        for identifier in license_info:
            # Query LicenseMaster for entries with matching SHORT_IDENTIFIER
            license_entry = LicenseMaster.objects.filter(short_identifier=identifier).first()
            
            # Append the result to the list
            if license_entry:
                license_objects.append(license_entry)
                
        return render(request, 'liclist.html', {'license_objects': license_objects})
    else:
        # Handle the case where license_infos is None
        return render(request, 'liclist.html', {'license_objects': []})

# export excel
class ExportToCSV(View):
    def get(self, request):
        file_id = request.session.get('file_id')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="SBOM_Vulnerability_List.csv"'
        writer = csv.writer(response)
        writer.writerow(['Vulnerability List'])
        writer.writerow(['Package Name', 'Version','CVE', 'CWE', 'Description', 'Risk Score', 'Risk Level']) 
        queryset = SbomVulData.objects.filter(file_id=file_id)
        queryset2 = SbomAppSbomData.objects.filter(file_id=file_id)
        
        for item in queryset:
            writer.writerow([item.product, item.version, item.cve, item.cwe, item.description, item.riskscore, item.risklevel])
        writer.writerow([' '])
        writer.writerow(['SBOM Detailed Information'])
        writer.writerow(['Package Name', 'Version','Originator', 'license', 'md5_hash', 'sha1_hash', 'sha256_hash'])
        for item2 in queryset2:
            writer.writerow([item2.name, item2.version, item2.originator, item2.license, item2.md5_hash, item2.sha1_hash, item2.sha256_hash])  

        return response
    
def main(request):
    
    return render(request, 'main.html')





