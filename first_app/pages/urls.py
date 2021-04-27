from django.urls import path
#from django.confg import settings
from .views import HomePageView, AboutPageView
#from django.conf.urls.sta

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),  # map to "" to HomePageView and name it to home
    path("about/", AboutPageView.as_view(), name="about"),  # appending about/
]