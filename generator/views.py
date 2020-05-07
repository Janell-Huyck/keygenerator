from django.shortcuts import render
from . import makekey


def generator(request):
    new_key = makekey.makekey()
    silly = 2
    return render(request, 'generator.html', {'new_key': new_key,
                                              'silly': silly})
