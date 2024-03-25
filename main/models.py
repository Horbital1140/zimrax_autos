from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AppInfo(models.Model):
    appname = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="logo")
    carousel1 = models.ImageField(upload_to="carousel")
    carousel2 = models.ImageField(upload_to="carousel")
    carousel3 = models.ImageField(upload_to="carousel")
    banner = models.ImageField(upload_to="banner")
    copyrights = models.IntegerField()

    def __str__(self):
        return self.appname


class Category(models.Model):
    Brand = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    photo = models.ImageField(upload_to="car_photo")

    def __str__(self):
        return self.Brand


class Product(models.Model):
    type = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )  # this argument "on_delete=models.CASCADE" is important when
    # using foreign key. foreign key is a relational field to relate to class together. e.g all car product in this class has category.
    #  e.g camry product belong to toyota category
    car_product = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True
    )  # this argument "unique=True" is important when using slungfiel
    color = models.CharField(
        max_length=50, default="a"
    )  # fieldname color was not included when we make last migration, so far
    # we intend to add "color" to the car, therefore we need to add (default="anywords"), if not added makemigration will not work

    # if you feel like you dont like having default as showing above in your model, after successful migration when default was added,
    # you can remove the above default='a', and run makemigration again. but it is optional to remove the default.
    year = models.IntegerField()
    seats = models.IntegerField()
    Register = models.BooleanField(
        default="True"
    )  # fieldname register was not included when we make last migration, so far
    # we intend to add "register" to the car, therefore we need to add (default="anywords"), if not added makemigration will not work
    # whatever you assign as default value i.e 'a' in above will show on the color field in the admin panel. then you can edit it
    # if you feel like you dont like having default as showing above in your model, after successful migration when default was added,
    # you can remove the above default='a', and run makemigration again. but it is optional to remove the default.

    price = models.FloatField()  # () meand required, information needs to be inputed
    promo_price = models.FloatField(
        blank=True, null=True
    )  # this arguement "blank=True, null=True" means not required, either information is provided or not it will be saved.
    car_photo = models.ImageField(upload_to="car_photo")
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )  # the argument "auto_now_add=True" display the date and time the info was
    # first uploaded,
    uploaded_at = models.DateTimeField(
        auto_now=True
    )  #  while "auto_now=True" display the time and date when the info was edited or updated.

    def __str__(self):
        return self.model


class Contact(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField(max_length=254)
    message_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Customer_registration(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # this line is compulsory, it ensure the django registration file recognize our own model for registration
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to="customer_photo")

    def __str__(self):
        return self.user.username





class Alt_pay(models.Model):
    acct_name = models.CharField(max_length=50)
    bnk_name = models.CharField(max_length=50)
    acct_number = models.IntegerField()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    paid = models.BooleanField()
    amount = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    amount = models.IntegerField()
    paid = models.BooleanField()
    phone_number = models.CharField(max_length=50)
    pay_code = models.CharField(max_length=50)
    additional_info = models.TextField()
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    
