from django.urls import path
from . import views
urlpatterns=[
    path('api/task',views.TaskList.as_view()),
    path('api/task/<int:pk>',views.TaskUpdate.as_view())
    
]