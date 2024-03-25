from django.urls import path
from main import views


urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("home", views.home, name="home"),
    path("product", views.product, name="product"),
    path("category/<str:id>/<slug:slug>", views.category, name="category"),
    path("detail/<str:id>/<slug:slug>", views.detail, name="detail"),
    path("signin", views.signin, name="signin"),
    path("signout", views.signout, name="signout"),
    path("contact", views.contact, name="contact"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("profile_update", views.profile_update, name="profile_update"),
    path("password_update", views.password_update, name="password_update"),
    path("landing_page", views.landing_page, name="landing_page"),
    path("search", views.search, name="search"),
    path("alt_pay", views.alt_pay, name="alt_pay"),
    path("add_to_cart", views.add_to_cart, name="add_to_cart"),
    path("cart", views.cart, name="cart"),
    path("delete", views.delete, name="delete"),
    path("update", views.update, name="update"),
    path("checkout", views.checkout, name="checkout"),
    path("pay", views.pay, name="pay"),
    path("callback", views.callback, name="callback"),
]
