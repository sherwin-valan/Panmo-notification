from django.urls import path
from .views import ExperimentCheckView

urlpatterns = [
    path('<int:pk>/check/', ExperimentCheckView.as_view(), name='experiment_check'),
]