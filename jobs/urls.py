from django.urls import path, include
from . import views
app_name = 'jobs'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('company/<int:pk>/', views.CompanyDetailView.as_view(),name='company-detail'),
    path('create/', views.company_review_create, name='create'),

    #path('select2/', include("django_select2.urls")),
    path('add/', views.JobApplicationCreateView.as_view(), name='add'),

    path('jobapplication/<int:pk>/delete', views.JobApplicationDeleteView.as_view(),name='job-application-delete'),
    path('jobapplication/<int:pk>/update', views.JobApplicationUpdateView.as_view(),name='job-application-update'),
]