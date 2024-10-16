from django.shortcuts import render,get_object_or_404,redirect
from .models import Item
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm,EditItemForm
from django.db.models import Q
# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk = pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    context = {'item':item,'related_items':related_items}
    return render(request,'item/detail.html',context)

@login_required
def new(request):
    form = NewItemForm()
    if(request.method=="POST"):
        form = NewItemForm(request.POST,request.FILES)
        if(form.is_valid()):
            item = form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('item:detail',pk=item.id)
    return render(request,'item/form.html',{'form':form})


@login_required
def delete(request,pk):
    item = get_object_or_404(Item, pk = pk,created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required
def edit(request,pk):
    item = get_object_or_404(Item, pk=pk,created_by=request.user)
    if(request.method=="POST"):
        form = EditItemForm(request.POST,request.FILES,instance = item)
        if(form.is_valid()):
            form.save()
            return redirect('item:detail',pk=item.id)
    form = EditItemForm(instance=item)
    return render(request,'item/form.html',{'form':form})


def items(request):
    items = Item.objects.filter(is_sold = False)
    query = request.GET.get('query')
    if(query):
        items = Item.objects.filter(Q(name__icontains = query) | Q(description__icontains=query))
    return render(request,'item/items.html',{'items':items})
