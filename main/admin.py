from django.contrib import admin


#from main.models import AppInfo, Category, Product, Contact, Customer_registration, Manual_payment  # instead of importing all the model class created, wildcard * can be use for all
# e.g from main.models import * instead of from main.models import AppInfo, Category, Product
from main.models import *
# Register your models here.
class AppInfoAdmin(admin.ModelAdmin):
    list_display = ['id','appname', 'copyrights']
    search_fields = ['id','appname', 'copyright']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('Brand',)}  # note class category return brand in model file
    list_display = ['id', 'Brand' ]
    search_fields = ['id', 'Brand']


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('model',)}  # note class product return model in model file
    list_display = ['id', 'type', 'model', 'year', 'seats', 'price', 'promo_price', 'uploaded_at', 'color', 'Register', 'car_product']
    search_fields = ['id', 'type', 'model', 'year', 'seats', 'price', 'promo_price', 'uploaded_at', 'color', 'Register', 'car_product']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'message', 'message_time']
    search_fields = ['id','name', 'email', 'message', 'message_time']


class Customer_registrationAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'email', 'username', 'last_name', 'city', 'phone_number']
    search_fields = ['id','first_name', 'email', 'username', 'last_name', 'city', 'phone_number']




class Alt_payAdmin(admin.ModelAdmin):
    list_display = ['id','bnk_name', 'acct_number', 'acct_name']
    search_fields = ['id','bnk_name', 'acct_number', 'acct_name']

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'car', 'price', 'quantity', 'paid', 'amount']
    search_fields = ['car', 'price', 'quantity', 'paid', 'amount']


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'amount', 'paid', 'phone_number', 'pay_code', 'payment_date']
    search_fields = ['id', 'user', 'first_name', 'last_name', 'amount', 'paid', 'phone_number', 'pay_code', 'payment_date']



 


admin.site.register(AppInfo, AppInfoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Customer_registration, Customer_registrationAdmin)
admin.site.register(Alt_pay, Alt_payAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Cart, CartAdmin)

