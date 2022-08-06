from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template("myapp1/index.html")
    context = {'fname':'Hanako'}
    return HttpResponse(template.render(context, request))
