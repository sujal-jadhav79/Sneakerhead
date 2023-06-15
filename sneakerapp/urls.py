from django.urls import path
from sneakerapp import views

urlpatterns = [
    path('about', views.about),
    # path('home', views.home),
    path('contact', views.contact),
    path('', views.index),
    path('delete/<rid>', views.delete),
    path('edit/<rid>', views.edit),
    path('addition/<x>/<y>', views.addition),
    # path('register',views.user_register),
    path('productlist', views.product_list),
    path('base', views.reuse),
    path('sort/<sv>', views.sort),
    path('catfilter/<catv>', views.catfilter),
    path('pricefilter/<pv>', views.pricefilter),
    path('pricerange', views.pricerange),
    path('pdetails/<pid>', views.product_details),
    path('addproduct', views.addproduct),
    path('delproduct/<rid>', views.delproduct),
    path('remove/<cid>', views.dc),  # remove from cart.
    path('remove1/<did>', views.dol),  # remove from placeorder
    path('editproduct/<rid>', views.editproduct),
    path('djangoform', views.djangoform),
    path('modelform', views.modelform),
    path('register', views.user_register),
    path('login', views.user_login),
    path('setsession', views.setsession),
    path('getsession', views.getsession),
    path('cart/<pid>', views.addtocart),
    path('logout', views.user_logout),
    path('viewcart', views.viewcart),
    path('changeqty/<pid>/<f>', views.changeqty),
    path('changeqtys/<pid>/<g>', views.changeqtys),
    path('placeorder', views.placeorder),
    path('payment', views.makepayment),
    path('store', views.storedetails),










]
