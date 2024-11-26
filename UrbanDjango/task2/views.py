from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Class_template(TemplateView):
    template_name = 'Class_template.html'


def func_template(request):
    return render(request, 'func_template.html')

