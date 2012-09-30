from django.shortcuts import render
from django.http import HttpResponseRedirect
from myapp.forms import MyModelForm
from myapp.models import MyModel

def form_request(request, url, template):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            request.session['name'] = name
            mm = MyModel.objects.create(name=name)
            mm.save()
            return HttpResponseRedirect(url) # Redirect after POST
    else:
        form = MyModelForm()
    args = {}
    objs = MyModel.objects.all()
    if objs:
        args['last_item'] = MyModel.objects.all().order_by('pk').reverse()[0]
    args['form'] = form
    return render(request, template, args)

def main(request):
    return form_request(request, '/add/', 'main.html')

def form_1(request):
    return form_request(request, '/1/', 'form_1.html')

def form_2(request):
    return form_request(request, '/2/', 'form_2.html')

def form_add(request):
    args = {}
    name = request.session['name']

    return render(request, 'add.html', args)
