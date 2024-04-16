from django.db import models
from django.contrib.postgres.fields import ArrayField  

class UploadedFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.FileField(upload_to='upload/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class SbomAppSbomData(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_id = models.BigIntegerField()
    name = models.TextField()
    version = models.TextField()
    originator = models.TextField()
    license_info = models.TextField()
    license = models.TextField()
    md5_hash = models.TextField()
    sha1_hash = models.TextField()
    sha256_hash = models.TextField()

    class Meta:
        managed = False
        db_table = 'sbom_app_sbom_data'

class SbomVulData(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_id = models.BigIntegerField()
    cve = models.CharField(db_column='cve', max_length=20, blank=True, null=True)
    product = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    riskscore = models.TextField()
    risklevel = models.TextField()
    cwe = models.TextField()

class SearcheData(models.Model):
    id = models.BigIntegerField(primary_key='True')
    cve_id = models.CharField(db_column='CVE_ID', max_length=20, blank=True, null=True)
    product = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'searche_data'

class ParsingCveData(models.Model):
    cve_id = models.CharField(db_column='CVE_ID', max_length=20, blank=True, null=True)
    cpe23uri = models.CharField(db_column='cpe23Uri', max_length=200, blank=True, null=True)
    versionstart = models.CharField(db_column='versionStart', max_length=100, blank=True, null=True)
    versionend = models.CharField(db_column='versionEnd', max_length=100, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'parsing_cve_data'

class CveData(models.Model):
    cve_id = models.CharField(db_column='CVE_ID', primary_key=True, max_length=20)
    data = models.TextField(db_column='DATA', db_collation='utf8mb4_bin') 
    class Meta:
        managed = False
        db_table = 'CVE_DATA'

class LicenseMaster(models.Model):
    license_id = models.AutoField(db_column='LICENSE_ID', primary_key=True, db_comment='라이선스ID')
    license_name = models.CharField(db_column='LICENSE_NAME', max_length=200, db_comment='라이선스 명') 
    license_type = models.CharField(db_column='LICENSE_TYPE', max_length=6, db_comment='라이선스 종류')
    obligation_disclosing_src_yn = models.CharField(db_column='OBLIGATION_DISCLOSING_SRC_YN', max_length=1, blank=True, null=True, db_comment='소스코드공개여부')
    obligation_notification_yn = models.CharField(db_column='OBLIGATION_NOTIFICATION_YN', max_length=1, blank=True, null=True, db_comment='고지여부')
    obligation_needs_check_yn = models.CharField(db_column='OBLIGATION_NEEDS_CHECK_YN', max_length=1, blank=True, null=True, db_comment='추후확인필요여부')
    short_identifier = models.CharField(db_column='SHORT_IDENTIFIER', max_length=100, blank=True, null=True, db_comment='라이선스 약어(SPDX기준인 경우만 설정)') 
    webpage = models.CharField(db_column='WEBPAGE', max_length=2000, blank=True, null=True, db_comment='라이선스를 만든 기관에서 제공하는 WEB PAGE 주소')
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True, db_comment='부가설명 및 collab link등') 
    license_text = models.TextField(db_column='LICENSE_TEXT', blank=True, null=True, db_comment='라이선스 원문')
    attribution = models.TextField(db_column='ATTRIBUTION', blank=True, null=True, db_comment='고지문구 추가 사항')  

    class Meta:
        managed = False
        db_table = 'LICENSE_MASTER'