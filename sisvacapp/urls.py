"""
URL configuration for sisvacapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('type/', include('apps.type.urls', namespace='type')),
    path('supplier/', include('apps.supplier.urls', namespace='supplier')),
    path('vaccine/', include('apps.vaccine.urls', namespace='vaccine')),
    path('person/', include('apps.person.urls', namespace='person')),
    path('clinic/', include('apps.clinic.urls', namespace='clinic')),
    path('session/', include('apps.session.urls', namespace='session')),
    path('professional/', include('apps.professional.urls', namespace='professional')),
    path('administrationroute/', include('apps.administrationroute.urls', namespace='administrationroute')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
