from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'api'
urlpatterns = [
    path('tasks/', views.TaskList.as_view(), name='tasks'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task'),
]

urlpatterns = format_suffix_patterns(urlpatterns)