from celery import shared_task
from django.core.management import call_command # NEW


@shared_task
def scan_db():
    call_command("initialize_db", )
