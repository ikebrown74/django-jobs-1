from django.contrib import admin

from wwu_housing.jobs.models import (AdminApplication, Applicant,
                                     Application, ApplicationComponentPart,
                                     ApplicationEmail, ApplicationStatus,
                                     Component, ComponentPart, Date, Job,
                                     JobUser, Qualification)


class ComponentInline(admin.TabularInline):
    model = Component


class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "open_datetime", "close_datetime",
                    "post_datetime")
    list_filter = ("open_datetime", "close_datetime")
    inlines = [ComponentInline]
    save_as = True
    save_on_top = True
admin.site.register(Job, JobAdmin)


class JobUserAdmin(admin.ModelAdmin):
    list_display = ("user", "job", "permission")
    list_filter = ("job",)
    ordering = ["user__username","job"]
admin.site.register(JobUser, JobUserAdmin)


class AdminApplicationAdmin(admin.ModelAdmin):
    list_display = ("status", "application")
admin.site.register(AdminApplication, AdminApplicationAdmin)


class ApplicationEmailAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "job")
    list_filter = ("job",)

admin.site.register(ApplicationEmail, ApplicationEmailAdmin)


class ApplicationStatusAdmin(admin.ModelAdmin):
    list_display = ("status", "weight")
admin.site.register(ApplicationStatus, ApplicationStatusAdmin)


class ComponentPartInline(admin.TabularInline):
    model = ComponentPart


class ComponentAdmin(admin.ModelAdmin):
    list_display = ("name", "job")
    list_filter = ("job",)
    inlines = [ComponentPartInline]
admin.site.register(Component, ComponentAdmin)


class ApplicantAdmin(admin.ModelAdmin):
    pass
admin.site.register(Applicant, ApplicantAdmin)


class ApplicationComponentPartInline(admin.TabularInline):
    model = ApplicationComponentPart


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("applicant", "job", "start_datetime", "end_datetime")
    list_filter = ("job", "start_datetime", "end_datetime")
    inlines = [ApplicationComponentPartInline]
admin.site.register(Application, ApplicationAdmin)


class DateAdmin(admin.ModelAdmin):
    list_display = ("job", "name", "date", "description")
    list_display_links = ("name",)
    list_filter = ("job", "date")
admin.site.register(Date, DateAdmin)


class QualificationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Qualification, QualificationAdmin)

