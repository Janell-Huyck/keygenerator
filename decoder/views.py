from django.shortcuts import render
from decoder.models import DecoderModel
from generator.models import GeneratorModel
# from generator/templates import templates


def index(request):
    generator = GeneratorModel.objects.all()
    # generator_html = generator/templates.generator.html
    decoder = DecoderModel.objects.all()
    return render(request, 'index.html', {
        'generator': generator,
        'decoder': decoder, })
