from django.urls import path, include

from apps.contacts import views

app_name = "contacts"

urlpatterns = [
    path("", views.ShowAllContactsView.as_view(), name='show_all'),
    path("create", views.ContactCreateView.as_view(), name='create'),
    path('<int:pk>/', include([
        path('edit', views.ContactUpdateView.as_view(), name='edit'),
        path('delete', views.DeleteContactsView.as_view(), name='delete')
    ])),
]
