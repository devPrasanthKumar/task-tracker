
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
# views
from django.views.generic import ListView, CreateView, FormView, DetailView,  UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# models
from taskTrackingApp.models import AndroidAppModel, TaskModel, UserProfileModel

# forms
from .forms import CreateAppForm, UpdateUserProfileForm

#
from django.db.models import Sum


class UpdateUserProfileView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("user-login")
    model = UserProfileModel
    form_class = UpdateUserProfileForm
    template_name = "create_profile.html"
    success_url = reverse_lazy("home")

    # checks the data if it is valid it will save to the db
    def form_valid(self, form):
        form.instance.user = self.request.user.userprofile.pk
        form.save()
        return super().form_valid(form)


class HomeView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("user-login")
    form_class = CreateAppForm
    model = AndroidAppModel
    success_url = reverse_lazy("home")
    template_name = "index.html"
    context_object_name = "app"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["apps"] = AndroidAppModel.objects.all()
        return context

    # admin can create apps and points
    def form_valid(self, form):
        '''
        this form can validate the data and saves them to the database,
        '''

        get_user = get_object_or_404(
            UserProfileModel, username=self.request.user.username)

        form.instance.user = get_user
        form.save()
        return super().form_valid(form)


# it will show the user's details
class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfileModel
    login_url = reverse_lazy("user-login")
    context_object_name = "showuserdetails"
    template_name = "normal_user/user_details.html"


# we can see the particular app's details
class ShowSingleAppView(DetailView, View):
    model = AndroidAppModel
    context_object_name = "singleapp"
    template_name = "normal_user/single_app.html"
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        '''
        here, it saves the data  to database when user uploads their task
        '''

        get_post_data = get_object_or_404(
            AndroidAppModel, pk=self.kwargs.get("pk"))
        get_user = get_object_or_404(UserProfileModel, user=self.request.user)
        uploaded_file = request.FILES.get('file')
        print(uploaded_file)

        TaskModel.objects.create(
            user=get_user, app=get_post_data, task_img=uploaded_file)
        return HttpResponse(" ")


class ShowCompletedTaskView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("user-login")
    template_name = "completed_task.html"
    context_object_name = "tasks"
    model = TaskModel

    def get_queryset(self):
        get_user = get_object_or_404(UserProfileModel, user=self.request.user)
        return TaskModel.objects.filter(user=get_user)


class ShowPointsView(ListView):
    model = AndroidAppModel
    template_name = "normal_user/user_points.html"
    context_object_name = "pointsapp"

    # pass the additional context data to the response page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["totalpoints"] = AndroidAppModel.objects.aggregate(
            total_points=Sum("points"))
        context["app_list"] = AndroidAppModel.objects.all()
        return context

    # override the queryset method..it will only show the data for the particular user who is currenly logged into the site
    def get_queryset(self):
        get_user = get_object_or_404(UserProfileModel, user=self.request.user)
        return AndroidAppModel.objects.filter(user=get_user)
