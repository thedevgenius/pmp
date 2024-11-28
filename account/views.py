from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .models import User, Team, TeamMember, Designation
from .forms import AddUserForm, LoginForm
from .decorators import is_leader

# Create your views here.

@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = "dashboard.html"
    def get_context_data(self, *args, **kwargs):
        context =  super(DashboardView, self).get_context_data(*args, **kwargs)
        if self.request.user.role == 'LD':
            context['team'] = self.request.user.team
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(is_leader, name='dispatch')
class MyMembers(TemplateView):
    template_name = 'users.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = Team.objects.get(user=self.request.user)
        context['members'] = TeamMember.objects.filter(team=team)
        return context
    
class MyLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('dashboard')
    redirect_authenticated_user = True



@method_decorator(login_required, name='dispatch')
@method_decorator(is_leader, name='dispatch')
class AddUserView(FormView):
    template_name = 'add_member.html'
    form_class = AddUserForm
    success_url = reverse_lazy('members')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        team = Team.objects.get(user=self.request.user)
        TeamMember.objects.create(
            team=team,
            member=user,
        )
        return super().form_valid(form)
