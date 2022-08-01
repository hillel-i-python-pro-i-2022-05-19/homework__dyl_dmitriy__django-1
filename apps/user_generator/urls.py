from django.urls import path

from apps.user_generator.views import GenerateUsersView

app_name = 'user_generator'

urlpatterns = [
    path('', GenerateUsersView.as_view(), name='index'),
    path('<int:users_count>', GenerateUsersView.as_view())
]
