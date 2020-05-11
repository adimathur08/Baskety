from django.shortcuts import render
from .models import item, catagory, usercart
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from shoppingCart.models import Profile, userorders, orderdetails


# Create your views here.
def landingPage(request):
    itemdata = item.objects.all()
    catt = catagory.objects.all()
    cart = usercart.objects.all().filter(user_id = request.user.id)
    return render(request, "landingPage.html", {'itemdata' : itemdata, 'catt':catt, 'cart':cart} )

def products(request):
    itemdata = item.objects.all()
    catt = catagory.objects.all()
    cart = usercart.objects.all().filter(user_id = request.user.id)
    return render(request, "products.html" , {'itemdata' : itemdata, 'catt':catt, 'cart':cart})

@login_required(login_url='/userhome')
def checkout(request):
    itemdata = item.objects.all()
    cart = usercart.objects.all().filter(user_id = request.user.id)
    total = 0
    for c in cart:
        for i in itemdata:
            if(i.id == c.product_id):
                total+= int(i.itemPrice * c.product_quantity)
    try:
        cart[0]
        cartempty=0
    except IndexError:
        cartempty=1
    return render(request, "checkout.html", { 'cart':cart, 'itemdata':itemdata, 'total':total,'cartempty':cartempty})

@login_required(login_url='/userhome')
def payment(request):
    # s=request.session.get('count')
    # request.session['count']=5
    itemdata = item.objects.all()
    cart = usercart.objects.all().filter(user_id = request.user.id)
    user_profile = Profile.objects.all().filter(user_id = request.user.id)
    user = user_profile[0]
    address = user.address
    phone = user.phone
    pincode = user.pincode
    total = 0
    for c in cart:
        for i in itemdata:
            if(i.id == c.product_id):
                total+= int(i.itemPrice * c.product_quantity)
    return render(request, "payment.html", {'total':total,'address':address, 'pincode':pincode, 'phone':phone, 'total':total})

@login_required(login_url='/userhome')
def addtocart(request):
    if request.method == "GET":
        return redirect('/')
    else:
        product_id = request.POST['itemid']
        product_quantity = 1
        print("HI post",request.POST.get("itemid"),"HI")
        cart = usercart.objects.all().filter(user_id = request.user.id, product_id = product_id )
        try:
            if cart[0] is not None:
            
                cart = usercart.objects.get(user_id = request.user.id, product_id=product_id)
                cart.product_quantity+=1
                cart.save()
                
            else:
                cart = usercart(product_id=product_id, user_id=request.user.id, product_quantity=product_quantity)
                cart.save()
        except IndexError:
                cart = usercart(product_id=product_id, user_id=request.user.id, product_quantity=product_quantity)
                cart.save()
        return redirect('checkout')

@login_required(login_url='/userhome')
def deleteitem(request):
    if request.method == "POST":
        product_id = request.POST['itemid']
        #usercart.objects.filter(user_id=request.user.id, product_id=product_id).delete()  #DELETES ALL
        user = usercart.objects.filter(user_id=request.user.id, product_id=product_id)
        user_data = user[0]
        if ( user_data.product_quantity > 1):
            user_data.product_quantity-=1
            user_data.save()
        elif user_data.product_quantity == 1:
            usercart.objects.filter(user_id=request.user.id, product_id=product_id).delete()
        return redirect('checkout.html')


@login_required(login_url='/userhome')
def orderdetail(request):
    orderid= request.GET.get('id')
    orderitems = orderdetails.objects.filter(order_id=orderid)
    allitems = item.objects.all()
    totalprice = 0
    for a in orderitems:
        for b in allitems:
            if(b.id == a.product_id):
                totalprice+= int(b.itemPrice * a.product_quantity)
    return render(request,'orderdetail.html',{'orderid':orderid,'orderitems':orderitems, 'allitems':allitems, 'totalprice':totalprice})

@login_required(login_url='/userhome')
def order_success(request):
    cartitems = usercart.objects.all().filter(user_id = request.user.id)
    itemdata = item.objects.all()
    total = 0
    quantity = 0
    for c in cartitems:
        for i in itemdata:
            if(i.id == c.product_id):
                total+= int(i.itemPrice * c.product_quantity)
                quantity+=1
    generateOrder = userorders(user_id = request.user.id, ammount=total, total_items= quantity)
    generateOrder.save()
    for cartitem in cartitems:
        saveitem = orderdetails(order_id = generateOrder.id, product_id = cartitem.product_id, product_quantity = cartitem.product_quantity, )
        saveitem.save()
        usercart.objects.filter(user_id=request.user.id, product_id=cartitem.product_id).delete()
    
    return render(request,'order_success.html',{'order_id':generateOrder.id})


@login_required(login_url='/userhome')
def orderhistory(request):
    orders = userorders.objects.filter(user_id = request.user.id)
    orders = orders.reverse()[:]
    return render(request,'orderhistory.html',{'orders':orders})


# def error_404(request, exception):
#     return render(request,"404.html")
    
# def error_500(request):
#     data = {}
#     return render(request,'404.html', data)