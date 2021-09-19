from django.urls import path

from .views import SignUpViews

urlpatterns = [
	path('signup/', SignUpView.as_view(), name='signup'),
]