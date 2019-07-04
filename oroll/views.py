from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import CreateUserForm, UploadForm
# Create your views here.

@login_required
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit = False)
            photo.owner = request.user
            form.save()
            return redirect('oroll:index')
    form = UploadForm()
    return render(request, 'oroll/upload.html', {'form':form})

class IndexView(ListView):
    # model = Photo
    context_object_name = 'user_photo_list'
    paginate_by = 10
    #template_name = 'oroll/index.html'

    def get_queryset(self):
        user = self.request.user
        return user.photo_set.all().order_by('-pub_date')

class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    #form_class = UserCreationForm
    success_url = reverse_lazy('create_user_done')

class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'


class ProfileView(DetailView):
    context_object_name = 'profile_user'
    model = User
    template_name = 'oroll/profile.html'
