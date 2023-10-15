from django.http import HttpResponse
import random
import time

def home(request):
    return HttpResponse("Hello, Django!")

def random_number(request):
    return HttpResponse(random.uniform(0, 1), status=200)

def user_number(request, number):
    if not number.isnumeric():
        return HttpResponse("Enter only numbers")
    else:
        number = int(number) #convert to int so we can do random on this number.
        return HttpResponse(random.uniform(0, number), status=200)

def current_time(request):
    return HttpResponse(time.strftime("%H:%M:%S"),time.localtime(), status = 200)

def len_word(request, word):
    if word.isalpha():
        return HttpResponse(len(word))
    else:
        return HttpResponse("enter only letters")
                