"""Student_Hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('questions.urls')),
    path('events/', include('events.urls')),
    path('', include('users.urls')),
    path('', include('notes.urls')),
    path('feedbacks/', include('feedbacks.urls'))
]
if (settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# Custom changes to django admin panel

admin.site.site_header = 'Student Hub Admin'
admin.site.site_title = 'Student Hub Admin Portal'
admin.site.index_title = 'Welcome to Student Hub Admin Portal'

# For Custom Error

# handler404 = 'users.views.my_custom_page_not_found_view'
# handler500 = 'users.views.my_custom_error_view'
handler403 = 'users.views.my_custom_permission_denied_view'
# handler400 = 'users.views.my_custom_bad_request_view'
