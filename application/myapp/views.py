from django.shortcuts import render
from .forms import ProjectForm
from django.core.mail import send_mail
# Create your views here.


def home(request):
    return render(request, "home.html")


def general(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            # Send email to the applicant
            # subject = 'Thank you for submitting your project'
            # message = 'Your project has been successfully submitted. We will review it shortly.'
            # recipient_email = form.cleaned_data['applicant_email']
            # send_mail(subject, message, None, [recipient_email])
    context = {'form': form}
    return render(request, "general.html", context)


def organization(request):
    return render(request, "organization.html")


def personnel(request):
    return render(request, "personnel.html")


def timeframe(request):
    return render(request, "timeframe.html")


def budget(request):
    return render(request, "budget.html")