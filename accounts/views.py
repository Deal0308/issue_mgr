from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')