from django.conf.urls.static import static
from django.urls import path
from products import views
from pyshop2 import settings


urlpatterns = [
    path("", views.index, name="index")
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
