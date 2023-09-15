from django.contrib import admin
from django.urls import path, include
from polls.views import ExperimentCheckView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
    path('', ExperimentCheckView.as_view(), name='home'),
]
