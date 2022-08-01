from django.urls import path, include

from apps.contacts import views

app_name = "contacts"

urlpatterns = [
    path("", views.show_all_contacts, name='show_all'),
    path("create", views.create_contacts, name='create'),
    path('<int:pk>/', include([
        path('edit', views.edit_contacts, name='edit'),
        path('delete', views.delete_contacts, name='delete')
    ])),
]
