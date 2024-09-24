from django.shortcuts import render, redirect
from django.http import HttpResponse
from appname.models import *

# Create your views here.

def register_page(request):
    context = {

    }

    if request.method == "POST":
        username = request.POST.get("username-field")
        password = request.POST.get("password-field")
        email = request.POST.get("email-field")

        User.objects.create(name = username, password = password, email = email)

    return render(
        request,
        template_name="register.html",
        context=context
    )

def login_page(request):

    context = {}

    if request.method == "POST":
        username = request.POST.get("username-field")
        password = request.POST.get("password-field")
        try:
            user = User.objects.get(name = username)
            if user.password == password:
                request.session['user_name'] = user.name
                return redirect('main_page')
            else:
                context = {"help": "Invalid password!"}
                return render(request, 'login.html', context=context)
        except:
            context = {"help": "Invalid username!"}
            return render(request, 'login.html', context=context)
    else:
        return render(
            request,
            template_name="login.html",
            context=context
        )

def main_page(request):
    current_user = User.objects.get(name = request.session.get('user_name'))
    hotels = Hotel.objects.all()
    context = {
        'user': current_user,
        'hotels': hotels,
    }
    return render(
        request,
        template_name="basic.html",
        context=context
    )
    
def hotel_page(request, hotel_name):
    hotel = Hotel.objects.get(name=hotel_name)
    rooms = hotel.rooms.all()
    context={
        "hotel":hotel,
        "rooms":rooms,
    }

    if request.method == "POST":
        current_user = User.objects.get(name = request.session.get('user_name'))
        room_id = request.POST.get("room-select")
        room = Room.objects.get(id=room_id)
        reservation_start = request.POST.get("start-time-select")
        reservation_end = request.POST.get("end-time-select")

        Reservation.objects.create(
                                reservation_start=reservation_start,
                                reservation_end= reservation_end,
                                room=room,
                                user=current_user)

    return render(
            request,
            template_name="hotel_page.html",
            context=context
    )

def room_page(request, room_id):

    room = Room.objects.get(id=room_id)
    context={
        "room":room,
    }

    return render(
            request,
            template_name="room_page.html",
            context=context
    )
