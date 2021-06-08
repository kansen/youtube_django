from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import HomePageView, AuthorizeView, Oauth2CallbackView, ProfileView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('authorize/', AuthorizeView.as_view(), name='authorize'),
    path('oauth2callback/', Oauth2CallbackView.as_view(),
         name='oauth2callback'),
    path('youtube/', ProfileView.as_view(), name="youtube"),
]

