from django.db import models

# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=255)
    # project_proposal = models.FileField(upload_to='project_proposals/')
    abstract = models.TextField()

    DURATION_CHOICES = [(2, 2), (3, 3)]
    project_duration = models.IntegerField(choices=DURATION_CHOICES)

    FIELD_CHOICES = [
        ('Natural studies', 'Natural studies'),
        ('Engineering and technology', 'Engineering and technology'),
        ('Medical and health sciences', 'Medical and health sciences'),
        ('Agricultural sciences', 'Agricultural sciences'),
        ('Social sciences', 'Social sciences'),
        ('Humanities', 'Humanities')

    ]
    field = models.CharField(max_length=50, choices=FIELD_CHOICES)
    keywords = models.CharField(max_length=100)
    undesirable_expert = models.CharField(max_length=100)

    organization_name = models.CharField(max_length=100, default="")
    organization_contact_person = models.CharField(max_length=50, default="")
    organization_contact_person_mail = models.EmailField(default="")

    applicant_name = models.CharField(max_length=50, default="")
    applicant_email = models.EmailField(default="")
    applicant_phone = models.CharField(max_length=25, default="")

    mentor_name = models.CharField(max_length=50, default="")
    mentor_email = models.EmailField(default="")
    mentor_phone = models.CharField(max_length=25, default="")



class ProjectDetails(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='project_details')
    # abstract = models.TextField()
    # project_duration = models.IntegerField(choices=[(2, 2), (3, 3)])
    # field = models.CharField(max_length=50, choices=[
    #     ('Natural studies', 'Natural studies'),
    #     ('Engineering and technology', 'Engineering and technology'),
    #     ('Medical and health sciences', 'Medical and health sciences'),
    #     ('Agricultural sciences', 'Agricultural sciences'),
    #     ('Social sciences', 'Social sciences'),
    #     ('Humanities', 'Humanities')
    # ])
    # keywords = models.CharField(max_length=100)
    # undesirable_expert = models.CharField(max_length=100)


class OrganizationDetails(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='organization_details')
    # organization_name = models.CharField(max_length=100, default="")
    # organization_contact_person = models.CharField(max_length=50, default="")
    # organization_contact_person_mail = models.EmailField(default="")


class ApplicantMentorDetails(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='applicant_mentor_details')
    # applicant_name = models.CharField(max_length=50, default="")
    # applicant_email = models.EmailField(default="")
    # applicant_phone = models.CharField(max_length=25, default="")
    # mentor_name = models.CharField(max_length=50, default="")
    # mentor_email = models.EmailField(default="")
    # mentor_phone = models.CharField(max_length=25, default="")
