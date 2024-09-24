from django.urls import path
import appname.views as views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("register", views.register_page, name="register_page"),
    path("login", views.login_page, name="login_page"),
    path('hotel/<str:hotel_name>/', views.hotel_page, name='hotel_page'),
    path('room/<int:room_id>/', views.room_page, name='room_page'),
]