from django.shortcuts import render,redirect
from .models import cart
from .models import pets
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Sum



# Create your views here.
def add_to_cart(request,id):
    cart_id = request.session.session_key
    if cart_id == None:
        cart_id = request.session.create()
    pet_data = pets.objects.get(id=id)
    price = pet_data.price
    user_data = request.user
    cart(cart_id=cart_id,pet=pet_data,user=user_data,totalprice=price).save()
    messages.success(request,"Item added to cart successfully")
    return redirect('/')

def cart_view(request):
    items = cart.objects.filter(user=request.user)
    flag = items.exists() 
    context = {
        'cart_items' : items,
        'flag' : flag
                }
    return render(request,'cart_view.html',context)

def cart_delete(request,id):
    cart_item=cart.objects.get(id=id)
    cart_item.delete()
    messages.success(request,"Item removed from cart successfully")
    return redirect('cart')

def update_cart(request,id):
    p = request.POST.get('price')
    # print("price", p)
    q = request.POST.get('qty')
    p_id = request.POST.get('id')
    total_price = float(p) * int(q)
    cart.objects.filter(id=p_id).update(quantity=q,totalprice=total_price)
    total_amount = cart.objects.filter(user=request.user).aaggregate(total=Sum('totalPrice'))['total'] or 0.0
    return JsonResponse ({'status':True,'totalprice':total_price})


