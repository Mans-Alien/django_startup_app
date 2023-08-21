from django.urls import path
from auth_app import views


urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.handle_login, name="handle_login"),
    path('logout/', views.handle_logout, name="handle_logout"),
]
