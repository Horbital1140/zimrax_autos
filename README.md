Our web-app was created to reduce the hassle of locating a trustworthy local auto seller, so we decided to work on creating a web application for car sales. An automobile firm's sales will soar when it has a web application that allows prospective buyers to see what it has in stock and be able to order and buy from the comfort of their homes. The web app will bolster the company’s online presence, thus spreading awareness and boosting car sales.

Our web-app was created to reduce the hassle of locating a trustworthy local auto seller, so we decided to work on creating a web application for car sales. An automobile firm's sales will soar when it has a web application that allows prospective buyers to see what it has in stock and be able to order and buy from the comfort of their homes. The web app will bolster the company’s online presence, thus spreading awareness and boosting car sales.

Core Algorithm and code snippet

User Authentication:

Django built-in authentication system was used. Though the Django default user registration can take a little user information, therefore, we ensure will imort Django User module and write a code that makes the default User work with our registreation model.

from django.contrib.auth import logout, login, authenticate
from .forms import ContactForm, Customer_registrationForm

Search and Filtering:
Django provides a powerful QuerySet API for searching and filtering data. Therefore, I use this API to ensure that users can filter cars base on their needs

Python

filtered_cars = Car.objects.filter(brand='Toyota')

