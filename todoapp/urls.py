from django.urls import path
from . import views
urlpatterns = [
    path('api/', views.todoappOverview, name="todoapp-overview"),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-Detail"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-create/', views.taskCreate, name="task-Create"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
  ]