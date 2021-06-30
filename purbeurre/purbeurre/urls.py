"""
purbeurre URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('', include('usermanage.urls')),
]

handler404 = 'webapp.views.error404'

