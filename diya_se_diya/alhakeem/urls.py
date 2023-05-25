from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
    path('', views.index, name='home'),
    path('donation', views.donation, name='donation'),
    path('home', views.home, name='home'),
    path('registration', views.registration, name='registration'),
    path('about', views.about, name='about'),
    path('team', views.team, name='team'),
    path('partner', views.partner, name='partner'),
    path('askforhelp', views.askforhelp, name='askforhelp'),
    path('saveusers', views.saveUsers, name='saveusers'),
    path('donationTaker', views.donationTaker, name='donationTaker'),

    path('application', views.application, name='application')
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)