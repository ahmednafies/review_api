"""product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r"", include("auth.urls")),
    url(r"", include("reviews.urls")),
    url(r"^api/", include("api.urls", namespace="api_v1")),
    url(r"^api/auth/$", obtain_jwt_token, name="api_login"),
    url(r"^admin/", admin.site.urls),
]

admin.site.site_header = "Review API Admin"
admin.site.site_title = "Review API Admin Portal"
admin.site.index_title = "Welcome to Hem's Review API Admin Portal"
