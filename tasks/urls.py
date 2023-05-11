from django.urls import path
from .views import IndexView, TaskDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:task_id>/',TaskDetailView.as_view(), name='view'),

]