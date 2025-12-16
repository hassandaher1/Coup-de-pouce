from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Back-office Django natif (optionnel, chemin différent)
    path("dj-admin/", admin.site.urls),

    # Interface publique + interface admin personnalisée
    path("", include("products.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
