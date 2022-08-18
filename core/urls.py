from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.phone_book.urls")),
    path("session", include("apps.sessions_example.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("users/", include("apps.users.urls")),
]
