from django.urls import path

from apps.user_generator.views import generate_users_view

app_name = 'user_generator'
urlpatterns = [
    path('', generate_users_view, name='index'),
    path('<int:users_count>', generate_users_view)
]
