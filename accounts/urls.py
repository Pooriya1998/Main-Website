from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    # login
    path('login', views.login_view, name='login'),
    # logout
    path('logout', views.logout_view, name='logout'),
    # registration / signup
    path('signup', views.signup_view, name='signup'),
]