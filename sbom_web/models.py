# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CveData(models.Model):
    cve_id = models.CharField(db_column='CVE_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    data = models.TextField(db_column='DATA', db_collation='utf8mb4_bin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CVE_DATA'


class LicenseMaster(models.Model):
    license_id = models.AutoField(db_column='LICENSE_ID', primary_key=True, db_comment='라이선스ID')  # Field name made lowercase.
    license_name = models.CharField(db_column='LICENSE_NAME', max_length=200, db_comment='라이선스 명')  # Field name made lowercase.
    license_type = models.CharField(db_column='LICENSE_TYPE', max_length=6, db_comment='라이선스 종류')  # Field name made lowercase.
    obligation_disclosing_src_yn = models.CharField(db_column='OBLIGATION_DISCLOSING_SRC_YN', max_length=1, blank=True, null=True, db_comment='소스코드공개여부')  # Field name made lowercase.
    obligation_notification_yn = models.CharField(db_column='OBLIGATION_NOTIFICATION_YN', max_length=1, blank=True, null=True, db_comment='고지여부')  # Field name made lowercase.
    obligation_needs_check_yn = models.CharField(db_column='OBLIGATION_NEEDS_CHECK_YN', max_length=1, blank=True, null=True, db_comment='추후확인필요여부')  # Field name made lowercase.
    short_identifier = models.CharField(db_column='SHORT_IDENTIFIER', max_length=100, blank=True, null=True, db_comment='라이선스 약어(SPDX기준인 경우만 설정)')  # Field name made lowercase.
    webpage = models.CharField(db_column='WEBPAGE', max_length=2000, blank=True, null=True, db_comment='라이선스를 만든 기관에서 제공하는 WEB PAGE 주소')  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True, db_comment='부가설명 및 collab link등')  # Field name made lowercase.
    license_text = models.TextField(db_column='LICENSE_TEXT', blank=True, null=True, db_comment='라이선스 원문')  # Field name made lowercase.
    attribution = models.TextField(db_column='ATTRIBUTION', blank=True, null=True, db_comment='고지문구 추가 사항')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LICENSE_MASTER'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoApschedulerDjangojob(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    next_run_time = models.DateTimeField(blank=True, null=True)
    job_state = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_apscheduler_djangojob'


class DjangoApschedulerDjangojobexecution(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=50)
    run_time = models.DateTimeField()
    duration = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    finished = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    exception = models.CharField(max_length=1000, blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    job = models.ForeignKey(DjangoApschedulerDjangojob, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_apscheduler_djangojobexecution'
        unique_together = (('job', 'run_time'),)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ParsingCveData(models.Model):
    cve_id = models.CharField(db_column='CVE_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cpe23uri = models.CharField(db_column='cpe23Uri', max_length=200, blank=True, null=True)  # Field name made lowercase.
    versionstart = models.CharField(db_column='versionStart', max_length=100, blank=True, null=True)  # Field name made lowercase.
    versionend = models.CharField(db_column='versionEnd', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parsing_cve_data'


class SbomAppSbomData(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_id = models.BigIntegerField()
    name = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    originator = models.TextField(blank=True, null=True)
    license_info = models.TextField(blank=True, null=True)
    license = models.TextField(blank=True, null=True)
    md5_hash = models.TextField(blank=True, null=True)
    sha1_hash = models.TextField(blank=True, null=True)
    sha256_hash = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbom_app_sbom_data'


class SbomAppSbomvuldata(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_id = models.BigIntegerField()
    product = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    cve = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    riskscore = models.TextField(blank=True, null=True)
    risklevel = models.TextField(blank=True, null=True)
    cwe = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sbom_app_sbomvuldata'


class SbomAppUploadedfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sbom_app_uploadedfile'


class SearcheData(models.Model):
    id = models.BigIntegerField()
    cve_id = models.CharField(db_column='CVE_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    product = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'searche_data'


class SearcheDataBackup(models.Model):
    id = models.BigAutoField(primary_key=True)
    cve_id = models.CharField(db_column='CVE_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    product = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'searche_data_backup'
