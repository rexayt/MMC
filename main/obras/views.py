from django.shortcuts import render

def main(request):
    return render(request,'main.html')

def artemoderna(request):
    return render(request,'arteModerna.html')

def olimpiada(request):
    return render(request, 'olimpiada.html')

def revIndustrial(request):
    return render(request, 'revIndustrial.html')

def santosDumont(request):
    return render(request, 'santosDumont.html')

def ingressos(request):
    return render(request, 'ingressos.html')

def login(request):
    return render(request, 'registration/login.html')

def sign_up(request):
    print(f"{request.POST.get('user')} {request.POST.get('email')} {request.POST.get('pass')}")
    return render(request, 'registration/sign_up.html')