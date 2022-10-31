from django.urls import path
from . import views
app_name = 'jobs'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('company/<int:pk>/', views.CompanyDetailView.as_view(),name='company-detail'),
    path('create/', views.company_review_create, name='create'),
    path('add/', views.job_application_create, name='add'),

    path('jobapplication/<int:pk>/delete', views.JobApplicationDeleteView.as_view(),name='job-application-delete'),
    path('jobapplication/<int:pk>/update', views.JobApplicationUpdateView.as_view(),name='job-application-update'),
]