"""
URL configuration for greenkiosk project.

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
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include("inventory.urls")),
    path('customer/', include("customer.urls")),
    path('delivery/', include("delivery.urls")),
    path('cart/', include("product_cart.urls")),
    path('orders/', include("orders.urls")),
    path('payment/', include("payment.urls")),
    path('refund/', include("refund.urls")),
    path('review/', include("reviews_and_rating.urls")),
    path('vendor/', include("Vendor.urls")),
    path('api/', include("api.urls"))





]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    