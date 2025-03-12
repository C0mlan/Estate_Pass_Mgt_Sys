from apscheduler.schedulers.background import BackgroundScheduler
from django.utils.timezone import now
from datetime import timedelta
from .models import Passer

#Delete code older than 1 minutes
def delete_old_passers():
    time_threshold = now() - timedelta(minutes=1)
    deleted_count, _ = Passer.objects.filter(created_at__lt=time_threshold).delete()
    print(f"[{now()}] Deleted {deleted_count} old Passer records.")

#starts the ApSchedular
def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(delete_old_passers, 'interval', minutes=1)
    scheduler.start()
