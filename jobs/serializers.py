#serializers file
from .models import Company, CompanyReview, JobApplication
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyReview
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'
    
    