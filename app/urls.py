from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("portfolio.urls")),
]

from .settings import DEBUG, MEDIA_ROOT, MEDIA_URL

if DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
