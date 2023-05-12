"""
URL configuration for MDZWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from pages import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("",views.home,name="home"),
    path("graphic designs/",views.graphic_designs,name="Graphic Designs"),
    path("web designs/",views.web_designs,name="Web Designs"),
    path("place order/",views.place_order,name="Place Order"),
    path("order details/",views.order_details,name="Order Details"),
    path("order/<slug:id>",views.order,name="Order"),
    path("delete/<slug:id>",views.delete_order,name="Delete Order")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
