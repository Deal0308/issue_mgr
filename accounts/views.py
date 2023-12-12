from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.urls import reverse_lazy
from .models import CustomUser

# Create your views here.
class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

class UserListView(ListView):
    model = CustomUser
    template_name = 'registration/user_list.html'
    context_object_name = 'users'

class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'registration/user_update.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'registration/user_delete.html'
    success_url = reverse_lazy('user_list')

class UserDetailView(TemplateView):
    model = CustomUser
    template_name = 'registration/user_detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = CustomUser.objects.get(pk=self.kwargs['pk'])
        return context
    
class UserCreateView(CreateView):
    model = CustomUser
    template_name = 'registration/user_create.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('user_list')


    

