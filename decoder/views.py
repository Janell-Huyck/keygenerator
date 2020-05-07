from django.shortcuts import render
from generator import makekey
from decoder import decodekey


def index(request):
    new_key = ''
    is_good_key = ''
    test_key = ''

    if(request.GET.get('test_button')):
        test_key = request.GET.get('test_key')
        is_good_key = decodekey.decodekey(request.GET.get('test_key'))
    if(request.POST.get('make_key')):
        new_key = makekey.makekey()
    return render(request, 'index.html', {'is_good_key': is_good_key,
                                          'test_key': test_key,
                                          'new_key': new_key})
