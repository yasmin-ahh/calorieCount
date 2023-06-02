from django.shortcuts import redirect, render
from .models import Food, Consume
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request): 
    
    consumed_food = None

    if request.user.id and request.method == "POST": 
        food_object = 0
        food_consumed = request.POST.get('food_consumed')
        try: 
            food_object = Food.objects.get(id=int(food_consumed))
            user = request.user
            consume = Consume(user=user, food_consumed=food_object)
            consume.save()
        except ObjectDoesNotExist: 
            pass
    if request.user.id: 
        consumed_food = Consume.objects.filter(user=request.user)
    foods = Food.objects.all()

    return render(request, 'mysite/index.html', {'foods': foods, 'consumed_food': consumed_food})

def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == "POST": 
        consumed_food.delete()
        return redirect('/')
    return render(request, 'mysite/delete.html')
    # except ObjectDoesNotExist: 
    #     pass
 
