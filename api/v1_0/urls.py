"""mozio_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url

from api.v1_0.supplier.views import SupplierList, SupplierDetail, PolygonList, PolygonDetail

urlpatterns = [
    url(r'^supplier/$', SupplierList.as_view()),
    url(r'^supplier/(?P<pk>[0-9]*)/$', SupplierDetail.as_view()),
    url(r'^polygon/$', PolygonList.as_view()),
    url(r'^polygon/(?P<pk>[0-9]*)/$', PolygonDetail.as_view()),
]
