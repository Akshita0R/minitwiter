from django.urls import path
from .views import IndexView, LoginView, SignupView, LogoutView, CreateTweetView, ProfileView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('signup', SignupView.as_view(), name='signup'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('createtweet', CreateTweetView.as_view(), name='createtweet'),
    path('profile', ProfileView.as_view(), name='profile')
]