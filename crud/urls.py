from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'crud'

urlpatterns = [
    path('user/', views.UserRegistration.as_view(), name='user_registration'),
    path('promocion/', views.PromocioListCreateView.as_view(),
         name='promocion_registration'),
    path('concurso/', views.ConcursoListCreateView.as_view(),
         name='concurso_registration'),
    path('excel/', views.ExcelParser.as_view(), name='excel'),
    path('hello/', views.Hello.as_view(), name='hello'),
    path('users/', views.UserList.as_view(), name='users')
]

urlpatterns = format_suffix_patterns(urlpatterns)
