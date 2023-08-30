from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Tweet
from .forms import LoginForm
from django.views.generic import View, ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

class IndexView(ListView):
    template_name = 'index.html'
    queryset = Tweet.objects.order_by('-id')
    context_object_name = 'tweets'

class LoginView(View):
    
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user:
                login(request, user)
                return redirect(reverse_lazy('index'))
            return render(request, 'login.html', {'form': form, 'message': 'Invalid username or password!'})

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('index'))

class CreateTweetView(CreateView):
    model = Tweet
    fields = ['description', 'image']
    template_name = 'createtweet.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # if not self.s:
        #     context['message'] = 'Signup unsuccessful!'
        return context

class ProfileView(ListView):
    template_name = 'profile.html'
    context_object_name = 'tweets'

    def get_queryset(self):
        return Tweet.objects.filter(user=self.request.user).order_by('-id')
