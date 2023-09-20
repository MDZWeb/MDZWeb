from django.shortcuts import render
from webdesigns.models import Webdesigns
from django.core.paginator import Paginator
# Create your views here.
def webdesigns(request):
    webdesigns_obj=Webdesigns.objects.filter(is_active=True)

    paginator=Paginator(webdesigns_obj,9)
    page=request.GET.get('page')
    webdesigns_obj_final=paginator.get_page(page)
    if page==None:
        page=1

    if page==None:
        page=1
    total_pages=int(paginator.num_pages)
    page_no_list=[]
    if int(paginator.num_pages)<=4:
        page_no_list=[ str(i) for i in range(1,total_pages+1)]

    if total_pages>4:
        if int(page)<=total_pages-3:
            if webdesigns_obj_final.has_previous():
                page_no_list=[int(page)-1,page,int(page)+1,"ellispe",total_pages]
            else:
                page_no_list=[page,int(page)+1,int(page)+2,"ellispe",total_pages]
        if int(page)>=total_pages-2:
            page_no_list=[str(i) for i in range(total_pages-3,total_pages+1,1)]

    data={
        "webdesigns":webdesigns_obj_final,
        'page_no_list':page_no_list,
        'page':page,
        
    }
    #print(webdesigns_obj_final,page_no_list,page)
    return render(request,'pages/web_designs.html',data)