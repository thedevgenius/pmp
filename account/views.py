from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import User
from .forms import AddUserForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .decorators import is_company
# Create your views here.

class DashboardView(TemplateView):
    template_name = "dashboard.html"



@method_decorator(is_company, name='dispatch')
class AddUserView(CreateView):
    model = User
    form_class = AddUserForm
    template_name = 'add_user.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.org = self.request.user
        user.save()
        return super().form_valid(form)
