from django.urls import path
from .views import RegisterUserView,LoginUserView,GoogleLoginView

urlpatterns=[
    path('register/',RegisterUserView.as_view(),name="register"),
    path('login/',LoginUserView.as_view(),name="login"),
    path('google/',GoogleLoginView.as_view(),name="google_auth")
]