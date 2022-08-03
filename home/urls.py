from django.urls import path
from . import views
from . views import CheckoutView

urlpatterns = [
    path('',views.index, name='index'),  
    path('categories',views.categories, name='categories'),  
    path('category/<str:id>/<slug:slug>',views.category, name='category'),  
    path('rooms',views.rooms, name='rooms'),  
    path('room/<slug:slug>',views.room, name='room'),
    path('contact', views.contact, name='contact'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('signout', views.signout, name='signout'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('profile_update', views.profile_update, name='profile_update'),
    path('password', views.password, name='password'),
    path('meeting', views.meeting, name='meeting'),
    path('swimming', views.swimming, name='swimming'),
    path('gym', views.gym, name='gym'),
    path('spa', views.spa, name='spa'),
    path('tennis', views.tennis, name='tennis'),
    path('fantasia', views.fantasia, name='fantasia'),
    path('salon', views.salon, name='salon'),
    path('booked', views.booked, name='booked'),
    path('booking', views.booking, name='booking'),
    path('cancel', views.cancel, name='cancel'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('pay', views.pay, name='pay'),
    path('callback', views.callback, name='callback'),
    path('change', views.change, name='change'),
     
]
