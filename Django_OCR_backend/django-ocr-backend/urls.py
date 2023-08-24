from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

admin.site.header_title = 'OCR App Administration'
admin.site.site_title = 'OCR App Administration'

urlpatterns = [
    #OAuth
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    # {
    #     "grant_type": "password",
    #     "username": "123456@qq.com",
    #     "password": "123456789",
    #     "client_id": "ulIMl0Ms2LnEEPNolZXnLB3HwziPbEIFRwMDlN2x",
    #     "client_secret":	"ghFnD3lvWejHiPZRNUV3fbMh5PG94CR2Fc6ukhGPyQaRrqNbbhKIR0MVTrxy40Y6Xcowg5pm6r4Ubm2xr6VZenJyuUpdemiFAgQl7PTsWaYb7OusG7HFO6kuMn0CLMUr"
    # }

    # OCR API Application
    path('api/', include('ocr.urls', namespace='ocr_api')),
    # Project URLs
    # For security purposes, the stock '/admin/' url has been changed
    path('factory/', admin.site.urls),
    # For additional security, standard '/admin/' changed to honeypot
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),

    # User Management
    path('api/user/', include('users.urls', namespace='users')),
    # {
    #     "email":"123456@qq.com",
    #     "username":"123456789",
    #     "password":"123456789"
    # }

    path('upload/<path>', serve, {'document_root':settings.UPLOAD_FILE})

]

# if settings.DEBUG:
#   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
