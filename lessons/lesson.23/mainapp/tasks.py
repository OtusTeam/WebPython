import time
from django_rq import job


def save_report(queryset):
    time.sleep(60)
    with open('food.txt', 'w', encoding='utf-8') as f:
        for food in queryset.all():
            f.write(f'{food.name}\n')


@job
def console_job():
    time.sleep(5)
    print('Hello from celery')
    return 156
