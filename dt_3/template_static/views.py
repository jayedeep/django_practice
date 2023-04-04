from django.shortcuts import render

# Create your views here.
def index(request):
    dummy_list=[
        'admin',
        'business',
        'merchant',
    ]
    return render(request,'index.html',{'random_text':'hello world','format':'%d-%b-%Y','dummy_list':dummy_list})
