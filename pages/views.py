from django.shortcuts import render,get_object_or_404,redirect
from GraphicDesigns.models import GraphicDesign
from django.core.paginator import Paginator
from WebPortfolios.models import Webportfolio
from Orders.models import Order

# Create your views here.

def home(request):
    graphic_designs_obj=GraphicDesign.objects.filter(is_feature=True)[0:3]
    webportfolio_obj=Webportfolio.objects.filter(is_feature=True)[0:3]

    data={
        'graphic_designs':graphic_designs_obj,
        'webportfolio':webportfolio_obj,
    }
    return render(request,'./pages/index.html',data)

def graphic_designs(request):
    

    graphic_designs_obj=GraphicDesign.objects.all()
    paginator=Paginator(graphic_designs_obj , 9)

    page=request.GET.get('page')
    graphic_designs_final=paginator.get_page(page)
    total_pages=graphic_designs_final.paginator.num_pages
    
    

    pages_list=[i for i in range(1,total_pages+1,1) ]

    if page ==None:
        page=1

    print(total_pages,page)

    if int(total_pages)<=4:
        pages_list=[i for i in range(1,total_pages+1)]
    
    if int(total_pages>=5):
        if (int(page)+2) < int(total_pages):
            pages_list=[i for i in range(int(page),(int(page)+3),9)]
            pages_list.append('ellipsis')
            pages_list.append(total_pages)

        else:
            pages_list=[i for i in range((int(total_pages)-3),int(total_pages)+1,1)]

    print(pages_list)

    graphic_designs_data={
        'graphic_designs':graphic_designs_final,
        'pages_list':pages_list,
        'page':page

    }



    return render (request,'./pages/graphic designs.html',graphic_designs_data)

def web_designs(request):

    Web_design_obj=Webportfolio.objects.all()
    paginator=Paginator(Web_design_obj , 9)

    page=request.GET.get('page')
    Web_design_final=paginator.get_page(page)
    total_pages=Web_design_final.paginator.num_pages
    
    

    pages_list=[i for i in range(1,total_pages+1,1) ]

    if page ==None:
        page=1

    print(total_pages,page)

    if int(total_pages)<=4:
        pages_list=[i for i in range(1,total_pages+1)]
    
    if int(total_pages>=5):
        if (int(page)+2) < int(total_pages):
            pages_list=[i for i in range(int(page),(int(page)+3),9)]
            pages_list.append('ellipsis')
            pages_list.append(total_pages)

        else:
            pages_list=[i for i in range((int(total_pages)-3),int(total_pages)+1,1)]

    print(pages_list)

    web_designs_data={
        'web_designs':Web_design_final,
        'pages_list':pages_list,
        'page':page

    }
    
    return render (request,'./pages/web designs.html',web_designs_data)

def place_order(request):
    Error_Flag=0
    Submit_Flag=0
    if request.method=="POST":
        if request.POST.get('first_name_v')=="" or request.POST.get('last_name_v')=="" or request.POST.get('email_v')=="" or request.POST.get('contact_v')=="" or request.POST.get('service_v')==None or request.POST.get('order_details_v')=="":
            Error_Flag=1
        else:
            first_name=request.POST.get('first_name_v')
            last_name=request.POST.get('last_name_v')
            email=request.POST.get('email_v')
            contact=request.POST.get('contact_v')
            service=request.POST.get('service_v')
            order_details=request.POST.get('order_details_v')
            print(first_name)
            print(first_name,last_name,email,contact,service,order_details)
            con=Order(First_name=first_name,Last_name=last_name,Email_id=email,Contact_no=contact,Service_type=service,order_detail=order_details)
            con.save()
            Submit_Flag=1

    print(Error_Flag)

    order_data={
        'Submit_Flag':Submit_Flag,
        'Error_Flag':Error_Flag,
    }

    return render (request,'./pages/place_order.html',order_data)




def order_details(request):
    data=[]
    order_obj=Order.objects.all().order_by('-Order_date')

    if request.method=="POST":
        search_type=request.POST.get('search_type')
        search_v=request.POST.get('search_v')

        for i in order_obj:
            if search_type=="Email Id" and search_v==i.Email_id or search_type=="Contact No" and search_v==i.Contact_no :
                data.append(i)
    order_data={
        'orders_data':data,
    }
    # try:
    #     for i in data:
    #         print(i.Email_id)
    # except:
    #     pass
    return render (request,'./pages/order_details.html',order_data)



def order(request,id):
    order_obj=get_object_or_404(Order,pk=id)

    order_data={
        'order_d':order_obj,
    }
    return render (request,'./pages/order.html',order_data)

def delete_order(request,id):
    event=Order.objects.get(pk=id)
    event.delete()
    return redirect('Place Order')
