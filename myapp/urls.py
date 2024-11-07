from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.home,name="my_home"),

    path('about/',views.about, name="about_us"),
    path('contact/',views.contact,name='our_contacts'),
    path('Services/',views.Services,name='our_services'),
    path('body/', views.body,name="my_body")
]
