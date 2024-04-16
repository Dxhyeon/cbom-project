# sbom_app/urls.py
from django.urls import path
from .views import FileUploadView
from . import views
from .views import ExportToCSV

urlpatterns = [
    path('', views.main, name='main'),
    path('index/', FileUploadView.as_view(), name='index'),
    path('sbomlist/', views.sbomlist, name='sbomlist'),
    path('vullist/', views.vullist, name='vullist'),
    path('liclist/', views.liclist, name='liclist'),
    path('export-csv/', ExportToCSV.as_view(), name='export_csv'),
] 