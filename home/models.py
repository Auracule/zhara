from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='category', default='category.jpg')
    description_c= models.TextField()
    min_price = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_r = models.CharField(max_length=50)
    img_r = models.ImageField(upload_to='room', default='room.jpg')
    room_no =models.CharField(max_length=5, default='a')
    price_r = models.IntegerField()
    adult_no = models.CharField(max_length=10)
    kids_no = models.CharField(max_length=10)
    description = models.TextField()
    economy = models.BooleanField()
    business = models.BooleanField()
    family = models.BooleanField()
    royals = models.BooleanField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name_r

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,null=True, blank=True)
    room_num = models.CharField(max_length=5, null=True, blank=True)
    price_b = models.FloatField(null=True, blank=True)
    check_in = models.DateField()
    check_out = models.DateField()
    no_days = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Gallery(models.Model):
    name = models.CharField(max_length=50)
    gallery = models.ImageField(upload_to='gallery', default= 'gallery.jpg')
    slide1 = models.BooleanField()
    slide2 = models.BooleanField()
    slide3 = models.BooleanField()

    def __str__(self):
        return self.name

    # class Meta:
    #     db_table = 'gallery'
    #     managed = True
    #     verbose_name = 'Gallery'
    #     verbose_name_plural = 'Gallery'
    
class Contact(models.Model):
    STATUS = [
        ('New', 'New'),
        ('Pending', 'Pending'),
        ('Done', 'Done'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    add_note = models.TextField()
    status = models.CharField(max_length=50, choices= STATUS, default= 'New')
    dated = models.DateField(auto_now=True)
    attended = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    state = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    pix = models.ImageField(upload_to='profile', default='avatar.png')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'profile'
        managed = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    