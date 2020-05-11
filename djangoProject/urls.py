from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from shoppingCart import views as shop_views

urlpatterns = [
    path('', include('shoppingCart.urls')),
    path('', include('userAccess.urls')),
    path('admin/', admin.site.urls),
]

# handler404 = shop_views.error_404
# handler500 = shop_views.error_500