from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from app1.views import    error_500
from django.conf.urls import  handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include("app1.urls"))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


handler500 = error_500    


