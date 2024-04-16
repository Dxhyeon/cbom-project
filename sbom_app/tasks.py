from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from datetime import timedelta
from .models import UploadedFile, SbomAppSbomData, SbomVulData
from django.conf import settings
from apscheduler.triggers.cron import CronTrigger

def perform_record_deletion():
    try:
        one_hour_ago = timezone.now() - timedelta(hours=1)
        
        file_ids = UploadedFile.objects.filter(uploaded_at__lte=one_hour_ago).values_list('id', flat=True)

        SbomAppSbomData.objects.filter(file_id__in=file_ids).delete()
        SbomVulData.objects.filter(file_id__in=file_ids).delete()
        
        records_to_delete = UploadedFile.objects.filter(uploaded_at__lte=one_hour_ago)
        records_to_delete.delete()
    except:
        exit
    
    print(f"DB 정리 완료 - {timezone.now()} ")

def start():
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_job(perform_record_deletion, 'cron', hour='*/3')

    scheduler.start()
    

