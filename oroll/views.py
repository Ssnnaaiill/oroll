from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
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

class IndexView(TemplateView):
    template_name = 'oroll/index.html'

class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    #form_class = UserCreationForm
    success_url = reverse_lazy('create_user_done')

class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'
