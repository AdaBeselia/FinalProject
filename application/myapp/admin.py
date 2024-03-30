from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import Project
from .models import ProjectDetails
from .models import OrganizationDetails
from .models import ApplicantMentorDetails

admin.site.register(Project)
admin.site.register(ProjectDetails)
admin.site.register(OrganizationDetails)
admin.site.register(ApplicantMentorDetails)