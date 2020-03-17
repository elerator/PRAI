"""lightweight_research_tool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
    path('projects/', include("projects.urls")),
    path('', include("landing_page.urls")),
    path('kanban/', include("kanban.urls")),
    path('capacities/', include("capacities.urls")),
    path('users/', include("users.urls")),
    path('exports/', include("exports.urls")),
] + static(settings.STATIC_SUFFIX, document_root=settings.STATIC_ROOT)#Necessary for deployment at sub root!!!!
