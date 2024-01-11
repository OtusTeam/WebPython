import time
from django.contrib import admin
import django_rq
from rq.job import Job

from .models import Animal, Category, Food, WildAnimal, HomeAnimal
from .tasks import save_report, console_job

admin.site.register(Category)


class FoodAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')

    @admin.action(description="Download Food")
    def download_food(self, request, queryset):
        # django_rq.enqueue(save_report, queryset=queryset)
        result = console_job.delay()
        print(result.id)
        with open('result_id.txt', 'w', encoding='utf-8') as f:
            f.write(result.id)
        # console_job()

    @admin.action(description="Get task result")
    def get_result(self, request, queryset):
        with open('result_id.txt', 'r', encoding='utf-8') as f:
            result_id = f.read()
            print(result_id)
            redis_conn = django_rq.get_connection()
            job = Job.fetch(result_id, redis_conn)
            if job.is_finished:
                ret = job.return_value()
            elif job.is_queued:
                ret = {'status': 'in-queue'}
            elif job.is_started:
                ret = {'status': 'waiting'}
            elif job.is_failed:
                ret = {'status': 'failed'}

            print('RET', ret)

    actions = [download_food, get_result]


admin.site.register(Food, FoodAdmin)

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'show_food')

admin.site.register(Animal, AnimalAdmin)

admin.site.register(WildAnimal, AnimalAdmin)


class HomeAnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'last_owner_name')

admin.site.register(HomeAnimal, HomeAnimalAdmin)
