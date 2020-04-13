from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserRegistration

app_name = 'crud'

urlpatterns = [
    path('user/', UserRegistration.as_view(), name='user_registration'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
