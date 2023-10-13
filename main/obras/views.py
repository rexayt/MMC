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