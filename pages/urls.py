from django.urls import path
from pages.views import registerView,loginView,letterView,homepageView,logoutView,secretSantaView

urlpatterns = [
    path('register/', registerView, name="register page"),
    path('', loginView, name="login page"),
    path('letter/', letterView, name="letter page"),
    path('home/', homepageView, name="home page"),
    path('logout/', logoutView, name="logout"),
    path('sercretsanta/', secretSantaView, name="secret santa"),

]