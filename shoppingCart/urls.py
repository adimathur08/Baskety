from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
     path( "", views.landingPage, name="landingPage"),
     path( "products.html", views.products, name="products"),
     path( "checkout.html", views.checkout, name="checkout"),
     path( "payment.html", views.payment, name="payment"),
     path( "addtocart", views.addtocart, name="addtocart"),
     path( "deleteitem", views.deleteitem, name="deleteitem"),
     path( "orderdetail", views.orderdetail, name="orderdetail"),
     path( "order_success", views.order_success, name="order_success"),
     path( "orderhistory", views.orderhistory, name="orderhistory")
     
     
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)