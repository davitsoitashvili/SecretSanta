from django.urls import path
from pages.views import registerView,loginView,letterView,homepageView,logoutView,secretSantaView

urlpatterns = [
    path('', homepageView, name="home page"),
    path('register/', registerView, name="register page"),
    path('login/', loginView, name="login page"),
    path('letter/', letterView, name="letter page"),
    path('logout/', logoutView, name="logout"),
    path('secretsanta/', secretSantaView, name="secret santa"),


]