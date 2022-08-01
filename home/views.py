import uuid
import requests
import json

from django.shortcuts import render,redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.views.generic import View
from . forms import *
from . models import *

# Create your views here.
def index(request):
    slide1 = Gallery.objects.filter(slide1=True)
    slide2 = Gallery.objects.filter(slide2=True)
    slide3 = Gallery.objects.filter(slide3=True)
    categories = Category.objects.all()

    context = {
        'slide1':slide1,
        'slide2':slide2,
        'slide3':slide3,
        'categories':categories,
    }

    return render(request, 'index.html', context)


def categories(request):
    categories = Category.objects.all()

    context = {
        'categories':categories,
    }

    return render(request, 'categories.html', context)


def category(request, id):
    single = Category.objects.get(pk = id)
    category = Room.objects.filter(category_id = id)
    context = {
        'category':category,
        'single':single,
    }
    return render(request, 'category.html', context)

def rooms(request):
    economy = Room.objects.filter(economy=True,available=True)[:4]
    family = Room.objects.filter(family=True,available=True)[:4]
    business = Room.objects.filter(business=True,available=True)[:4]
    royals = Room.objects.filter(royals=True,available=True)[:4]

    context = {
        'economy':economy,
        'family':family,
        'business':business,
        'royals':royals,
    }

    return render(request, 'rooms.html', context)

def room(request, id):
    room = Room.objects.get(pk=id)

    context = {
        'room':room,
    }

    return render(request, 'room.html', context)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent Successfully!')
        return redirect('index')
    return render(request, 'index.html')


def contacts(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'message sent successfully')
            return redirect('contacts')
    return render(request, 'contacts.html')



def signout(request):
    logout(request)
    return redirect('signin')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Signin SUccessful!')
            return redirect('index')
        else:
            messages.error(request, 'invalid username/password. Kindly Check and signin again')
            return redirect('signin')
    return render(request, 'signin.html')

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        address = request.POST['address']
        state = request.POST['state']
        phone = request.POST['phone']
        pix = request.POST['pix']
        form = SignupForm(request.POST)
        if form.is_valid():
            newuser = form.save()
            newprofile = Profile(user=newuser)
            newprofile.first_name = newuser.first_name
            newprofile.last_name = newuser.last_name
            newprofile.email = newuser.email
            newprofile.address = address
            newprofile.phone = phone
            newprofile.state = state
            newprofile.pix = pix
            newprofile.save()
            login(request, newuser)
            messages.success(request, 'Signup Successful!')
            return redirect('index')
        else:
            messages.error(request, form.errors)
            return redirect('signup')
    return render(request, 'signup.html')

@login_required(login_url='signin')
def profile(request):
    profile = Profile.objects.get(user__username= request.user.username)

    context = {
        'profile':profile,
    }
    return render(request, 'profile.html', context)

@login_required(login_url='signin')
def profile_update(request):
    profile = Profile.objects.get(user__username = request.user.username)
    update = ProfileUpdate(instance= request.user.profile)

    if request.method == 'POST':
        update = ProfileUpdate(request.POST, request.FILES, instance= request.user.profile)
        if update.is_valid():
            update.save()
            messages.success(request, 'Profile Update Successful!')
            return redirect('profile')
        else:
            messages.error(request, update.errors)
            return redirect('profile_update')

    context = {
        'profile':profile,
        'update':update,
    }

    return render(request, 'profile_update.html', context)

@login_required(login_url='signin')
def password(request):
    profile = Profile.objects.get(user__username= request.user.username)
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password Change SuccessFul!')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('password')
    context = {
        'profile':profile,
        'form':form,
    }

    return render(request, 'password.html', context)

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def meeting(request):
    return render(request, 'meeting.html')

def swimming(request):
    return render(request, 'swimming.html')

def tennis(request):
    return render(request, 'tennis.html')

def salon(request):
    return render(request, 'saloon.html')

def gym(request):
    return render(request, 'gym.html')

def spa(request):
    return render(request, 'spa.html')

def fantasia(request):
    return render(request, 'fantasia.html')

@login_required(login_url='signin')
def booking(request):
    if request.method == 'POST':
        checkin = request.POST['checkin']
        checkout = request.POST['checkout']
        room = request.POST['roomid']
        room_id = Room.objects.get(pk=room)
        room_no = Profile.objects.get(user__username= request.user.username)
        order_no = room_no.id

        room = Booking.objects.filter(user__username= request.user.username, paid=False)
        if room:
            reserve = Booking.objects.filter(room= room_id.id,check_in = checkin,check_out = checkout, user__username= request.user.username)
            if reserve:
                reserve.check_in = checkin
                reserve.check_out = checkout
                if reserve.check_in > checkout or reserve.check_out < checkin:
                    reserve.save()
                    messages.success(request, 'Room Successfully reservered!')
                    return redirect('booked')
                else:
                    messages.warning(request, 'The room you requested is not available for these dates!')
                    return redirect('rooms')
            else:
                newroom = Booking()
                newroom.user= request.user
                newroom.room = room_id
                newroom.price_b= room_id.price_r
                newroom.check_in = checkin
                newroom.check_out = checkout
                newroom.paid= False
                newroom.save()
                messages.success(request, 'Room reserve Successfully')
                return redirect('rooms')
        else:
            newroom = Booking()
            newroom.user= request.user
            newroom.room = room_id
            newroom.price_b= room_id.price_r
            newroom.check_in = checkin
            newroom.check_out = checkout
            newroom.paid= False
            newroom.save()
            messages.success(request, 'Room reserve successful')
            return redirect('rooms')
    return redirect('rooms')

@login_required(login_url='signin')
def booked(request):
    booked= Booking.objects.filter(user__username= request.user.username, paid=False)
    profile = Profile.objects.get(user__username= request.user.username)
    
    for item in booked:
        item.no_days = (item.check_out - item.check_in).days
        item.amount = item.price_b * item.no_days
        item.save()

    subtotal = 0
    vat = 0
    total = 0

    for item in booked:
        subtotal += item.price_b * item.no_days

    vat =  0.075 * subtotal

    total = subtotal + vat

    context = {
        'booked':booked,
        'profile':profile,
        'subtotal':subtotal,
        'total':total,
        'vat':vat,
    }

    return render(request, 'booked.html', context)

@login_required(login_url='signin')
def change(request):
    if request.method == 'POST':
        new = request.POST['new']
        chck_in = request.POST['chckin']
        chck_out = request.POST['chckout']
        roomm = Booking.objects.get(pk= new)
        roomm.check_in = chck_in
        roomm.check_out = chck_out
        roomm.save()
    return redirect('booked')

@login_required(login_url='signin')
def cancel(request):
    room = request.POST['roomid']
    booked_id = Booking.objects.get(pk=room)
    booked_id.delete()
    messages.success(request, 'reservation successfully cancelled!')
    return redirect('booked')

# integrating axios API/ using class based view./  without function based view
class CheckoutView(View):
    def get(self, request):
        booked = Booking.objects.filter(user__username= request.user.username, paid=False)
        profile = Profile.objects.get(user__username= request.user.username)

        subtotal= 0
        vat = 0
        total = 0

        for item in booked:
            subtotal = item.price_b * item.no_days

        vat =  0.075 * subtotal

        total = subtotal + vat

        context = {
            'booked':booked,
            'profile':profile,
            'total':total,     
        }
        return render(request, 'checkout.html', context)

@login_required(login_url='signin')
def pay(request):
    if request.method == 'POST':
        api_key = 'sk_test_43762140e809dbc5ffee4d9c1e84d8c72afd6b9d'
        curl = 'https://api.paystack.co/transaction/initialize'
        # cburl = 'http://127.0.0.1:8000/callback'
        cburl = 'http://44.204.34.42/callback'
        user = User.objects.get(username= request.user.username)
        email = user.email
        total = float(request.POST['total']) * 100
        owner = user.profile.id
        transac_code = str(uuid.uuid4())
        headers = {'Authorization':f'Bearer {api_key}'}
        data = {'reference':transac_code, 'email':email, 'amount':int(total), 'order_number':owner, 'callback_url':cburl, 'currency':'NGN'}

        try:
            r = requests.post(curl, headers= headers, json= data)
        except Exception:
            messages.error(request, 'Network busy, refresh and try again')
        else:
            trans_back = json.loads(r.text)
            rdurl = trans_back['data']['authorization_url']
        return redirect(rdurl)
    return redirect('booked')

def callback(request):
    profile = Profile.objects.get(user__username= request.user.username)
    booked = Booking.objects.filter(user__username= request.user.username, paid=False)

    for item in booked:
        item.paid = True
        item.save()

        book_owner = Room.objects.get(pk=item.room.id)
        book_owner.available = False
        book_owner.save()

    context = {
        'profile':profile,
        'booked':booked,
    }

    return render(request, 'callback.html', context)





 