from django.urls import path, include
from . import views
from rest_framework import routers
app_name = 'jobs'

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'companyreviews', views.CompanyReviewViewSet)
router.register(r'jobapplications', views.JobApplicationViewSet)

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    

    path('company/<int:pk>/', views.CompanyDetailView.as_view(),name='company-detail'),
    path('create/', views.company_review_create, name='create'),

    #path('select2/', include("django_select2.urls")),
    path('add/', views.JobApplicationCreateView.as_view(), name='add'),

    path('jobapplication/<int:pk>/delete', views.JobApplicationDeleteView.as_view(),name='job-application-delete'),
    path('jobapplication/<int:pk>/update', views.JobApplicationUpdateView.as_view(),name='job-application-update'),
]

urlpatterns += router.urls


#ON 5.3 OF https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c

