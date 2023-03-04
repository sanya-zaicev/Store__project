
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from products.views import *
from store import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='index'),
    path('categories/', include('products.urls')),
    path('users/', include('users.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls')),]