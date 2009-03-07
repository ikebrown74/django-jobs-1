from django.contrib import admin

from wwu_housing.jobs.models import Job, Applicant, Application, Date, \
                                    Component, ApplicationComponent, \
                                    Qualification


class ComponentInline(admin.TabularInline):
    model = Component


class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "open_datetime", "close_datetime", "description", 
                    "post_datetime")
    list_filter = ("open_datetime", "close_datetime")
    inlines = [ComponentInline]
    save_as = True
    save_on_top = True
admin.site.register(Job, JobAdmin)


class ApplicantAdmin(admin.ModelAdmin):
    pass
admin.site.register(Applicant, ApplicantAdmin)


class ApplicationComponentInline(admin.TabularInline):
    model = ApplicationComponent


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("applicant", "job", "start_datetime", "end_datetime")
    list_filter = ("job", "start_datetime", "end_datetime")
    inlines = [ApplicationComponentInline]
admin.site.register(Application, ApplicationAdmin)


class DateAdmin(admin.ModelAdmin):
    list_display = ("job", "name", "date", "description")
    list_display_links = ("name",)
    list_filter = ("job", "date")
admin.site.register(Date, DateAdmin)


class QualificationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Qualification, QualificationAdmin)
