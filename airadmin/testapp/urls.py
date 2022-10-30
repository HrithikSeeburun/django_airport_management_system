from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
   path("", views.home),
   path('login_page', views.login_page),
   path('loadin', views.loadin),
   path('employee_registration', views.employee_registration),
   path('employee_register', views.employee_register),
   path('manager_registration', views.manager_registration),
   path('manager_register', views.manager_register),
   path('airport', views.load_airport),
   path('employee', views.load_employee),
   path('flight', views.load_flight),
   path('runway', views.load_runway),
   path('shop', views.load_shop),
   path('airline_register', views.add_airline),
   path('add_airline_company', views.load_airlineadd),
   path('add_flight', views.load_flightadd),
   path('flight_register', views.add_flight),
   path('immigration_register', views.add_immigration),
   path('add_immigration', views.load_immigrationadd),
   path('passenger_register', views.add_passenger),
   path('add_passenger', views.load_passengeradd),
   path('runway_register', views.add_runway),
   path('add_runway', views.load_add_runway),
   path('airline_company', views.load_airline_company),
   path('immigration', views.load_immigration),
   path('add_item', views.add_item),
   path('load_add_item', views.load_add_item),
   path('load_passenger',views.load_passenger),
   path('return', views.load_return)
]
