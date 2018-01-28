from django.shortcuts import render
from fakenewsFE.test import predict
from fakenewsFE.tocsv import text2csv
from fakenewsFE.google_searcher import start_predict
from fakenewsFE.check_site import checker

# Create your views here.
def index(request):
    if 'ArticleS' in request.POST:
        screenname = request.POST.get("Article", None)
        text2csv(screenname)
        display=predict('fakenewsFE\data.csv')
        if(display<0):
            display=0.001
        display=str(('%0.2f' % display))+" % True"
        return render(request, 'output.html' ,{'output': display})

    if 'KeyWordS' in request.POST:
        screenname1 = request.POST.get("KeyWord", None)
        print(screenname1)
        predict1=start_predict(screenname1)
        predict1=float(predict1)*100
        predict1=str(predict1)+" % True"
        return render(request, 'output.html' ,{'output': predict1})
        
    if 'WebsiteS' in request.POST:
        screenname2 = request.POST.get("Website", None)
        predict2 = checker(screenname2)
        print(predict2)
        return render(request, 'output.html' ,{'output': predict2})
    return render(request,'index.html')
