from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("apps.base.urls")),
    path("user-generator/", include("apps.user_generator.urls")),
    path("caesar/", include("apps.caesar.urls")),
    path("contacts/", include("apps.contacts.urls")),
    path("sessions/", include("apps.session_storage.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("users/", include("apps.users.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
