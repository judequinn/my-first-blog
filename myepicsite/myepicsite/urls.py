from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site


urlpatterns = [
	
	url(r'^admin/filebrowser/', include(site.urls)),
	url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
