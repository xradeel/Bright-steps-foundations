from django.shortcuts import render
from .models import users

# Create your views here.
def index(request):
    return render(request ,'index.html')

def donation(request):
    return render(request, 'donate_form.html')

def home(request):
    return render(request, 'index.html')

def registration(request):
    return render(request, 'registration_form.html')

def about(request):
    return render(request, 'about_us.html')

def team(request):
    return render(request, 'our_team.html')

def partner(request):
    return render(request, 'partners.html')


def askforhelp(request):
    return render(request, 'askforhelp.html')

def application(request):
    return render(request, 'applications.html')

def saveUsers(request):
    if request.method== 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        en= users(firstName=fname, lastName=lname, email=email, phone=phone)
        en.save()

    return render(request, 'index.html')

def donationTaker(request):
    if request.method== 'POST':
        fullName = request.POST.get('fullname')
        uniName = request.POST.get('uniName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city= request.POST.get('city')
        state = request.POST.get('state')
        requirement = request.POST.get('requirement')
        detailsReq = request.POST.get('detailReq')
        capability = request.POST.get('capability')
        anythingelse = request.POST.get('anythinelse')

        en= users(fullName=fullName, uniName=uniName, email=email, phone=phone, address=address, city=city, state= state, requirement=requirement, detailsReq=detailsReq, capability=capability, anythingelse=anythingelse)
        en.save()

    return render(request, 'index.html')