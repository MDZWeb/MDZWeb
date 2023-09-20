from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from MDZWeb import settings
import uuid
from order.models import Order
# Create your views here.

def placeorder(request):
    if request.method=="POST":
        first_name_v=request.POST.get("first_name_v")
        last_name_v=request.POST.get("last_name_v")
        username=f"{first_name_v} {last_name_v}"
        email_v=request.POST.get("email_v")
        contact_v=request.POST.get("contact_v")
        service_v=request.POST.get("service_v")
        order_details_v=request.POST.get("order_details_v")
        #print(first_name_v,last_name_v,email_v,contact_v,service_v,order_details_v,uuid.uuid4(),uuid.uuid4().hex[:7].upper())

        if service_v==None:
            messages.error(request,"Please Select Service Type")
            return redirect("placeorder")

        else:
            order_obj=Order.objects.create(
                first_name=first_name_v,
                last_name=last_name_v,
                user_name=username,
                email=email_v,
                contact=contact_v,
                service=service_v,
                order_details=order_details_v,
            )

            order_obj.save()
            order_id_value=f"{uuid.uuid4().hex[:7].upper()}-{order_obj.id}"
            order_obj.order_id= order_id_value
            order_obj.save()

            try:
                subject = 'Welcome to MDZ Web'
                message = f'Hi {username} !\nYour Order has been Placed.\nAnd Your order id is!\nOrder ID : {order_id_value}\nYou can track your order by using this Id.\nOur Team will also contact you soon'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email_v,'dawoodzahid127@gmail.com']
                #print(subject,message,email_from,recipient_list)
                send_mail( subject, message, email_from, recipient_list )
            except:
                pass
            messages.success(request,"Your Order has been placed successfully. Our Team will contact you soon!")
            return redirect("order_details_id",order_id=order_id_value)

    return render(request,'pages/place_order.html')


def order_details(request):
    order_obj=None
    if request.method=="POST":
        search_type=request.POST.get("search_type")
        search_v=request.POST.get("search_v")
        #print(search_type,search_v)
        
        if search_type=='EmailId':
            order_obj=Order.objects.filter(email=search_v).order_by('-id')
        if search_type=='ContactNo':
            order_obj=Order.objects.filter(contact=search_v).order_by('-id')
        if search_type=='OrderId':
            order_obj=Order.objects.filter(order_id=search_v).order_by('-id')
        if len(order_obj)<1 or order_obj==None:
            messages.error(request,"No Result Found")
            return redirect('order_details')
    data={
        'orders':order_obj,
    }
        

    return render(request,'pages/order_details.html',data)

def order_details_id(request,order_id=None):
    if order_id!=None:
        order_obj=Order.objects.filter(order_id=order_id)
        data={
            'orders':order_obj,
        }
        return render(request,'pages/order_details.html',data)
    else:
        messages.error(request,"There is some error. Please Try again")
        return redirect("placeorder")

def details(request,order_id=None):
    order_obj=None
    if order_id!=None:
        # order_obj=Order.objects.get(order_id=order_id)
        order_obj=get_object_or_404(Order,order_id=order_id)
        
    data={
        'orders':order_obj,
    }
    return render(request,'pages/order.html',data)


def delete(request,order_id=None):
    order_obj=None
    if order_id!=None:
        try:
            order_obj=Order.objects.get(order_id=order_id)
        except:
            pass
        order_obj.delete()
        messages.success(request,"Order has been deleted Successfully!. Now you can place new order.")
        return redirect("placeorder")