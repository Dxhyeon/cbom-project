import json
import re
import os

# SPDX .spdx
def SPDX(file_path):
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, '..', 'file_path', file_path)
    file = open(file_path,'r',encoding='utf-8')
    f = file.read()

    info = []
    name = []
    version = []
    license_info = []
    license = []
    md5_hash = []
    sha1_hash = []
    sha256_hash = []
    originator = []

    # Package Name append
    info = re.findall(r'PackageName:\s*(.+)', str(f))
    for input_str in info:
        str_replace = input_str.replace("/","-")
        str_replace = str_replace.replace("\\","-")
        str_replace = str_replace.replace("@","")
        name.append(str_replace)

    # Version append
    version = re.findall(r'PackageVersion:\s*(.+)', str(f))
    
    # orifinator append
    originator = re.findall(r'PackageOriginator:\s*(.+)', str(f))

    # License Info 
    PackageLicenseInfoFromFiles = re.findall(r'PackageLicenseInfoFromFiles:\s*(.+)', str(f))
    license_info.append(PackageLicenseInfoFromFiles[0].split())

    # License append
    license = re.findall(r'PackageLicenseDeclared:\s*(.+)',str(f))

    # md5 hash append
    md5_hash = re.findall(r'PackageChecksum: MD5:\s*(.+)',str(f))

    # sha1 hash append
    sha1_hash = re.findall(r'PackageChecksum: SHA1:\s*(.+)',str(f))

    # sha256 hash append
    sha256_hash = re.findall(r'PackageChecksum: SHA256:\s*(.+)',str(f))

    # None
    for i in range(len(license), len(name)):
        originator.append(None)
        license.append(None)
        md5_hash.append(None)
        sha1_hash.append(None)
        sha256_hash.append(None)

    return name, version, license_info, license, originator, md5_hash, sha1_hash, sha256_hash






# SPDX JSON .spdx
def SPDX_JSON(file_path):

    with open(file_path, 'r',encoding='utf-8') as file:
        f = json.load(file)
    name = []
    version = []
    license_info = []
    license = []
    md5_hash = []
    sha1_hash = []
    sha256_hash = []
    originator = []
    length = len(f["packages"])

    # Name append
    for i in range(0, length):
        name.append(f["packages"][i]["name"])

    # Version append
    for j in range(0, length):
        version.append(f["packages"][j]["versionInfo"])
    
    # orifinator append
    for l in range(0, length):
        try:
            if f["packages"][l]["originator"]:
                originator.append(f["packages"][l]["originator"])
        except:
            originator.append(None)

    # License Info 
    license_info = f["packages"][0]["licenseInfoFromFiles"]

    # License append
    for k in range(0, length):
        try:
            if f["packages"][k]["licenseDeclared"]:
                license.append(f["packages"][k]["licenseDeclared"])
        except:
            license.append(None)
    
    # md5 hash append
    for a in range(0, length):
        try:
            if f["packages"][a]["checksums"][0]["checksumValue"]:
                md5_hash.append(f["packages"][a]["checksums"][0]["checksumValue"])
        except:
            md5_hash.append(None)
    
    # sha1 hash append
    for b in range(0, length):
        try:
            if f["packages"][b]["checksums"][1]["checksumValue"]:
                sha1_hash.append(f["packages"][b]["checksums"][1]["checksumValue"])
        except:
            sha1_hash.append(None)

    # sha256 hash append
    for c in range(0, length):
        try:
            if f["packages"][c]["checksums"][2]["checksumValue"]:
                sha256_hash.append(f["packages"][c]["checksums"][2]["checksumValue"])
        except:
            sha256_hash.append(None)

    return name, version, license_info, license, originator, md5_hash, sha1_hash, sha256_hash






# cycloneDX .json

def cyDX_JSON(file_path):

    with open(file_path, 'r',encoding='utf-8') as file:
        f = json.load(file)

    info =[]
    name = []
    version = []
    license_info = []
    license = []
    md5_hash = []
    sha1_hash = []
    sha256_hash = []
    originator = []
    length = len(f["components"])

    # Package Name and Version
    for i in range(0,length):
        info.append(f["components"][i]["bom-ref"])

    pattern = r'\/\S+'

    for input_str in info:
        matches = re.findall(pattern, input_str)
        str_matches = ''.join(matches)
        str_matches = str_matches.replace("/","")
        parts = str_matches.split("@")
        name.append(parts[0])
        version.append(parts[1])
    
    # orifinator append
    pattern = r'pkg:(\w+)/'
    for input_str in info:
        originator += re.findall(pattern, input_str)

    
    # License Info 
    for i in range(0, len(f["metadata"]["component"]["licenses"])):
        try:
            license_info.append(f["metadata"]["component"]["licenses"][i]["license"]["id"])
        except:
            continue
    
    # License append
    for i in range(0, length):
        try:
            license.append(f["components"][i]["licenses"][0]["license"]["id"])
        except:
            license.append(None)

    # cyclone hash not supported
    for i in range(length):
        md5_hash.append(None)
        sha1_hash.append(None)
        sha256_hash.append(None)        
    

    return name, version, license_info, license, originator, md5_hash, sha1_hash, sha256_hash
    