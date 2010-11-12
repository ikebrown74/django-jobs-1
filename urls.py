from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list

from models import Job
from views import admin, applicant, application, component, job


urlpatterns = patterns("",
    url(r"^$", object_list, {"queryset": Job.objects.posted(), "template_object_name": "job"}, name="jobs_index"),
    url(r"^(?P<job_slug>[-\w]+)/$", job, name="jobs_job"),
    url(r"^(?P<job_slug>[-\w]+)/admin/$", admin, name="jobs_job_admin"),
    url(r"^(?P<job_slug>[-\w]+)/admin/(?P<applicant_slug>[-\w]+)/$", applicant, name="jobs_job_admin_applicant"),
    url(r"^(?P<job_slug>[-\w]+)/application/$", application, name="jobs_application"),
    url(r"^(?P<job_slug>[-\w]+)/application/(?P<component_slug>[-\w]+)/$", component, name="jobs_component")
)
