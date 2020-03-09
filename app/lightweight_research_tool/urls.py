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

site_root = "prai_information_desk/"
urlpatterns = [
    path(site_root + 'admin/', admin.site.urls),
    path(site_root + 'projects/', include("projects.urls")),
    path(site_root + '', include("landing_page.urls")),
    path(site_root + 'kanban/', include("kanban.urls")),
    path(site_root + 'capacities/', include("capacities.urls")),
    path(site_root + 'users/', include("users.urls")),
]
