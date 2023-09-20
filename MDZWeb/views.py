from django.shortcuts import redirect,render
from graphicdesigns.models import Graphic_Designs
from webdesigns.models import Webdesigns
def home(request):
    graphicdesigns_obj=Graphic_Designs.objects.filter(is_active=True,is_feature=True).order_by('-id')[0:6]
    webdesigns_obj=Webdesigns.objects.filter(is_active=True,is_feature=True).order_by('-id')[0:3]
    
    data={
        "graphicdesigns":graphicdesigns_obj,
        "webdesigns":webdesigns_obj,
    }
    return render(request,'pages/index.html',data)


def page404(request,exception):
    return render(request,'pages/page_404.html',{})