from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from akshayaindiawebsite import views as akshayaindiawebsite_views
from django.conf.urls import handler404, handler500
from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('akshayaindiawebsite.urls') ),
    path('dashboard/', include('dashboard.urls', namespace="DashBoard")),
   
    path('ckeditor_uploader/', include('ckeditor_uploader.urls')),
    url(r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = akshayaindiawebsite_views.error_404