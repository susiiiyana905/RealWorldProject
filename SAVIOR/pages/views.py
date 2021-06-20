from django.shortcuts import render

# Create your views here.

def home_page(request):
    context={
        'activate_home':'active'
    }

    return render(request, 'pages/home.html',context)

