
from django.urls import path
from . import views
urlpatterns = [
    path("",views.login,name="login"),
    path("index/",views.index,name="index"),
    path("createacc/",views.createacc,name="createacc"),
    path("about/",views.about,name="about"),
    path("Contact/",views.Contact,name="Contact"),
    path("quickview/<int:myid>",views.quickview,name="quickview"),
    path("track/",views.track,name="track"),
    path("checkout/",views.checkout,name="checkout"),
    path("search/",views.search,name="search"),
    path("adress/",views.adress,name="adress"),
    path("review/",views.review,name="review"),
    path("payment/",views.payment,name="payment"),
    path("cart/",views.cart,name="cart"),
    path("info/",views.info,name="info"),
    path("su/",views.su,name="su")
]
