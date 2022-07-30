from . models import *

def category(request):
    categories = Category.objects.all()

    context = {
        'categories':categories,
    }
    return context