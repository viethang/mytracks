from django.urls import path

from . import views

urlpatterns = [
  path('', views.UserListView.as_view()),
  path('<int:user_id>/email_validation/', views.email_validation)
]
