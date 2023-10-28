from django.shortcuts import render
from .models import pets
from django.http import Http404
from django.db.models import Q


# Create your views here.


def pets_list(request):
    all_products = pets.objects.all()
    context = {
        'objects':all_products

    }
    return render(request,'petsapp/list.html',context)

def dog_list(request):
    dog_list = pets.objects.filter(animal_type='D')
    all_dog_data = {
        'objects':dog_list


    }
    return render(request,'petsapp/doglist.html',all_dog_data)

def cat_list(request):
    cat_list = pets.objects.filter(animal_type='c')
    all_cat_data = {
        'objects':cat_list


    }
    return render(request,'petsapp/catlist.html',all_cat_data)

def pet_detail(request,pk):
    query = pets.objects.get(id=pk)
    context = {
        'objects':query
    }
    return render(request,'petsapp/pet_detail.html',context)

def search(request):
    if request.method == "GET":
        searched_data = request.GET.get('search')
        if (len(searched_data)==0):
            raise Http404
        else:
            query = (Q(name__icontains=searched_data) | 
            Q(species__icontains=searched_data) | Q(breed__icontains=searched_data))

            result = pets.objects.filter(query)
            context = {
                'objects': result

            }
        return render (request,'petsapp/search.html',context)
    else:
        raise Http404


