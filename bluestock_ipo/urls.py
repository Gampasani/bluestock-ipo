from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ipo.views import ipo_list_view, ipo_detail_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ipo_list_view, name='home'),
    path('ipo/<int:pk>/', ipo_detail_page_view, name='ipo-detail-page'),
    path('api/', include('ipo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
