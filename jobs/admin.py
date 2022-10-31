from django.contrib import admin
from .models import Company, CompanyReview, JobApplication
# Register your models here.


admin.site.register(Company)
admin.site.register(CompanyReview)
admin.site.register(JobApplication)




'''

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','logo']
    list_filter = ['name']

@admin.register(CompanyReview)
class CompanyReviewAdmin(admin.ModelAdmin):
    list_display = ['star_rating','user','position','notes','created']
    list_filter = ['created']

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['user','company','stage','date_applied']
    list_filter = ['date_applied']

'''