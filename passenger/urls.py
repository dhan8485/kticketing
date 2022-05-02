from django.urls import path
from . import views
urlpatterns=[
    path('index',views.home ),
    path('bookticket',views.UserBooking)

]