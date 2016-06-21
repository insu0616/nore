from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^english/', include('englishnote.urls', namespace='english')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', lambda request: redirect('/english')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)