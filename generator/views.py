from django.shortcuts import render


def generator(request):
    return render(request, 'generator.html')
