import requests
import uuid
import json


from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import *
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import *
from django.db.models import Q


# Create your views here.


def home(request):
    # info = AppInfo.objects.get(pk=2)  this is a manual placement of our appinfo on each page of the website,check context.processor.py and add it to settings.py
    cat = Category.objects.all()

    context = {
        #   'info':info,  this is a manual placement of our appinfo on each page of the website,check context.processor.py and add it to settings.py
        "cat": cat
    }

    return render(request, "index.html", context)


def landing_page(request):
    # info = AppInfo.objects.get(pk=2) this is a manual placement of our appinfo on each page of the website,check context.processor.py and add it to settings.py

    # context = {
    #'info':info,  this is a manual placement of our appinfo on each page of the website,check context.processor.py and add it to settings.py

    # }
    return render(request, "landingpage.html")


def product(request):
    car_product = Product.objects.all().order_by(
        "price"
    )  # order by is added to show a field name in the model that determine the display of the vehicles
 
    p = Paginator(
        car_product, 6
    )  # p is a variable that command paginator to display only 6 cars on a page out of all the cars displayed by the variable car product
    page = request.GET.get(
        "page"
    )  # page is a variable that sent get request when paginator page is called i.e previous, 1,2,3,next
    pagin = p.get_page(
        page
    )  # pagin is a variable that use get_page method to get the next six product on page.

    # info = AppInfo.objects.get(pk=2)  this is a manual placement of our appinfo on each page of the website,check context.processor.py and add it to settings.py

    context = {
        # 'car_product':car_product, was commented or removed because car_product has become a parameter inside p, and p has been called by pagin, therefore pagin replace car_product in the context
        "pagin": pagin,
        #'info':info,  this is a manual placement of our appinfo on each page of the website,check context.processor.py and add it to settings.py
    }
    return render(request, "product.html", context)


def category(request, id, slug):
    carbrand = Category.objects.get(pk=id)
    caritem = Product.objects.filter(type_id=id)

    context = {
        "carbrand": carbrand,
        "caritem": caritem,
    }

    return render(request, "category.html", context)


def detail(request, id, slug):
    cardetail = Product.objects.get(pk=id)

    context = {
        "cardetail": cardetail,
    }

    return render(request, "detail.html", context)


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "your messages has been sent successfully")
            return redirect("home")

    # info = AppInfo.objects.get(pk=2)     this is a manual placement of our appinfo on each page of the website,check context.processor.py and add it to settings.py
    context = {
        "form": form,
        #  'info':info,  this is a manual placement of our appinfo on each page of the website,check context.processor.py and add it to settings.py
    }

    return render(request, "contact.html", context)


def signout(request):
    logout(request)
    messages.success(request, "Dear client, you have sign out successfully")
    return redirect("signin")


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Dear Client, you have successfully login")
            return redirect("home")
        else:
            messages.error(
                request,
                "username/password is incorrect, please enter correct login details",
            )
            return redirect("signin")

    """   
   # info = AppInfo.objects.get(pk=2)    this is a manual placement of our appinfo on each page of the website,check context.processor.py and add it to settings.py 
    context = {
            
            'info':info,  this is a manual placement of our appinfo on each page of the website,check context.processor.py and add it to settings.py
        }
       """
    return render(request, "login.html")


def register(request):
    register = Customer_registrationForm()
    if request.method == "POST":
        # calling out the label in our model thatnis not in django register form creation
        username = request.POST["username"]
        city = request.POST["city"]
        phone_number = request.POST["phone_number"]
        profile_picture = request.POST["profile_picture"]
        # calling out stop

        register = Customer_registrationForm(request.POST)
        if register.is_valid():
            user = register.save()
            newuser = Customer_registration(user=user)
            newuser.first_name = user.first_name
            newuser.last_name = user.last_name
            newuser.email = user.email
            newuser.phone_number = phone_number
            newuser.username = username
            newuser.city = city
            newuser.profile_picture = profile_picture
            newuser.save()
            messages.success(
                request,
                f"dear {user.username} your account has been created succesfully",
            )
            return redirect("signin")
        else:
            messages.error(request, register.errors)
    """
    info = AppInfo.objects.get(pk=2)    
    context = {
            
            'info':info,
        }
        
    """

    return render(request, "register.html")




@login_required(login_url='signin')
def profile(request):
    userprof = Customer_registration.objects.get(user__username=request.user.username)

    context = {"userprof": userprof}

    return render(request, "profile.html", context)

@login_required(login_url='signin')
def profile_update(request):
    userprof = Customer_registration.objects.get(user__username=request.user.username)
    pform = ProfileForm(instance=request.user.customer_registration)
    if request.method == "POST":
        pform = ProfileForm(
            request.POST, request.FILES, instance=request.user.customer_registration
        )
        if pform.is_valid():
            user = pform.save()
            new = user.first_name.title()
            messages.success(
                request, f"dear {new} your profile has been updated successfully!"
            )
            return redirect("profile")
        else:
            new = user.first_name.title()
            messages.success(
                request,
                f"dear {new} your profile update generate the following error: {pform.errors}",
            )
            return redirect("profile_update")

    context = {
        "userprof": userprof,
    }

    return render(request, "profile_update.html", context)



@login_required(login_url="signin")
def password_update(request):
    userprof = Customer_registration.objects.get(user__username=request.user.username)
    form = PasswordChangeForm(request.user)
    if request.method == "POST":
        new = (
            request.user.username.title()
        )  # this line is called because we want the username to appear in the success and error messages
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, f"dear {new} your password has been changed successfully.!!"
            )
            return redirect("profile")

        else:
            messages.error(
                request,
                f"dear {new} there is an error in changing your password. {form.errors}",
            )
            return redirect("password_update")

    context = {"userprof": userprof, "form": form}

    return render(request, "password_update.html", context)










@login_required(login_url='signin')
def search(request):
    if request.method == "POST":
        items = request.POST["search"]
        searched = Q(
            Q(model__icontains=items)
            | Q(year__icontains=items)
            | Q(color__icontains=items)
            | Q(price__icontains=items)
            | Q(seats__icontains=items)
            | Q(Register__icontains=items)
            | Q(car_product__icontains=items)
            | Q(uploaded_at__icontains=items)
            
        )
        searched_item = Product.objects.filter(searched)

        context = {"items": items, "searched_item": searched_item}

        return render(request, "search.html", context)

    else:
        return render(request, "search.html")



@login_required(login_url='signin')
def alt_pay(request):
    alt = Alt_pay.objects.all()

    context = {"alt": alt}

    return render(request, "ade.html", context)



@login_required(login_url='signin')
def add_to_cart(request):
    if request.method == "POST":
        quantity = int(request.POST["quantity"])
        carid = int(request.POST["carid"])
        main = Product.objects.get(pk=carid)
        cart = Cart.objects.filter(user__username=request.user.username, paid=False)
        if cart:
            basket = Cart.objects.filter(
                user__username=request.user.username,
                paid=False,
                car=main.id,
                quantity=quantity,
            ).first()
            if basket:
                basket.quantity += quantity
                basket.amount = main.price * basket.quantity
                basket.save()
                messages.success(request, "one item added to cart")
                return redirect("product")
            else:
                new_item = Cart()
                new_item.user = request.user
                new_item.car = main
                new_item.quantity = quantity
                new_item.price = main.price
                new_item.amount = main.price * quantity
                new_item.paid = False
                new_item.save()
                messages.success(request, "one item added to cart successfully")
                return redirect("product")

        else:
            new_cart = Cart()
            new_cart.user = request.user
            new_cart.car = main
            new_cart.quantity = quantity
            new_cart.price = main.promo_price
            new_cart.amount = main.price * quantity
            new_cart.paid = False
            new_cart.save()
            messages.success(request, "one item added to cart successfully")
            return redirect("product")
    


@login_required(login_url='signin')
def cart(request):
    cart = Cart.objects.filter(user__username=request.user.username, paid=False)
    for item in cart:
        item.amount = item.price * item.quantity
        item.save()

    subtotal = 0
    vat = 0
    total = 0

    for item in cart:
        subtotal += item.price * item.quantity
        vat = 0.075 * subtotal
        total = subtotal + vat

    context = {"cart": cart, "subtotal": subtotal, "vat": vat, "total": total}

    return render(request, "cart.html", context)

@login_required(login_url='signin')
def delete(request):
    if request.method == "POST":
        del_item = request.POST["delid"]
        Cart.objects.filter(pk=del_item).delete()
        messages.success(request, "one item deleted successfully")
        return redirect("cart")



@login_required(login_url='signin')
def update(request):
    if request.method == "POST":
        qty_item = request.POST["quantid"]
        new_qty = request.POST["quant"]
        newqty = Cart.objects.get(pk=qty_item)
        newqty.quantity = new_qty
        newqty.amount = newqty.price * newqty.quantity
        newqty.save()
        messages.success(request, "quantity updated")
        return redirect("cart")



@login_required(login_url='signin')
def checkout(request):
    userprof = Customer_registration.objects.get(user__username=request.user.username)
    cart = Cart.objects.filter(user__username=request.user.username, paid=False)
    for item in cart:
        item.amount = item.price * item.quantity
        item.save()

    subtotal = 0
    vat = 0
    total = 0

    for item in cart:
        subtotal += item.price * item.quantity
        vat = 0.075 * subtotal
        total = subtotal + vat

    context = {
        "cart": cart,
        "subtotal": subtotal,
        "vat": vat,
        "total": total,
        "userprof": userprof,
    }
    return render(request, "checkout.html", context)



@login_required(login_url='signin')
def pay(request):
    if request.method == "POST":

        api_key = 'sk_test_072baf1ffa4979c55048cd7079d6b7fe022472e8'  # secret key from payment gateway
        curl = 'https://api.paystack.co/transaction/initialize'  # call url from payment gateway
        cburl = 'http://127.0.0.1:8000/callback'  # payment thank you page from our template, i.e call_back page
        ref = str(
            uuid.uuid4()
        )  # refrence number required by payment gatewayas an additional order number
        profile = Customer_registration.objects.get(
            user__username=request.user.username
        )
        order_no = profile.id  # main order number
        total = (
            float(request.POST["total"]) * 100
        )  # total amount to be charged from customer card
        user = User.objects.get(
            username=request.user.username
        )  # query the user model for customer details
        email = user.email  # store customer email to send to payment gateway
        first_name = request.POST[
            "first_name"
        ]  # collect from the template incase there is change
        last_name = request.POST[
            "last_name"
        ]  # collect from the template incase there is change
        phone_number = request.POST[
            "phone_number"
        ]  # collect from the template incase there is change
        add_info = request.POST[
            "add_info"
        ]  # collect from the template incase there is change

        # collect data to send to payment gateway via call
        headers = {"Authorization": f"Bearer {api_key}"}
        data = {
            "reference": ref,
            "amount": int(total),
            "email": user.email,
            "callback_url": cburl,
            "order_number": order_no,
            "currency": "NGN",
        }

        # MAKE A CALL TO PAYMENT GATEWAY
        try:
            r = requests.post(curl, headers=headers, json=data)
        except Exception:
            messages.error(request, "network busy, please try again later")
        else:
            transback = json.loads(r.text)
            rdurl = transback["data"]["authorization_url"]

            account = Payment()
            account.user = user
            account.first_name = user.first_name
            account.last_name = user.last_name
            account.amount = total / 100
            account.paid = True
            account.phone_number = phone_number
            account.additional_info = add_info
            account.pay_code = ref
            account.save()

            return redirect(rdurl)
    return redirect("checkout")



@login_required(login_url='signin')
def callback(request):

    userprof = Customer_registration.objects.get(user__username=request.user.username)
    cart = Cart.objects.filter(user__username=request.user.username, paid=False)

    for item in cart:
        item.paid = True
        item.save()

        car = Product.objects.get(pk=item.car.id)

    context = {"userprof": userprof, "cart": cart, "car": car}

   
    return render(request, "callback.html", context)
