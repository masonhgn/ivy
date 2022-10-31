from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CompanyReviewForm, JobApplicationForm
from .models import JobApplication, CompanyReview, Company
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
@login_required
def company_review_create(request):
    if request.method == 'POST':
        form = CompanyReviewForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.save()
            messages.success(request, 'Review has been posted.')
            return redirect('/')
            #return redirect(new_review.company.get_absolute_url())
    else:
        form = CompanyReviewForm(data=request.GET)
    return render(request,'jobs/job/create_review.html', {'section':'jobs','form':form})

@login_required
def job_application_create(request):
    if request.method == 'POST':
        form = JobApplicationForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_job_application = form.save(commit=False)
            new_job_application.user = request.user
            new_job_application.save()
            messages.success(request, 'New job application added.')
            return redirect('/')
    else:
        form = JobApplicationForm(data = request.GET)
    return render(request,'jobs/job/jobapplication_form.html',{'section': 'jobs','form': form})

@login_required
def homepage(request):
    #return render(request, 'home/homepage.html', {'section': 'homepage'})
    context = {
        'applications' : JobApplication.objects.filter(user = request.user),
    }
    return render(request,'home/homepage.html', context)


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'jobs/job/company_detail.html'

class CompanyReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CompanyReview
    success_url = reverse_lazy('homepage')
    def test_func(self):
        CompanyReview = self.get_object()
        if self.request.user == CompanyReview.user:
            return True
        return False

class JobApplicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = JobApplication
    template_name = 'jobs/job/jobapplication_confirm_delete.html'
    success_url = reverse_lazy('homepage')
    def test_func(self):
        JobApplication = self.get_object()
        if self.request.user == JobApplication.user:
            return True
        return False


class JobApplicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = JobApplication
    template_name = 'jobs/job/jobapplication_form.html'
    success_url = reverse_lazy('homepage')
    fields = ['stage', 'date_applied']
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def test_func(self):
        JobApplication = self.get_object()
        if self.request.user == JobApplication.user:
            return True
        return False


