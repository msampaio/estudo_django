from django.shortcuts import render
from django.http import HttpResponseRedirect
from myapp.forms import MyModelForm
from myapp.models import MyModel

def main(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            request.session['name'] = name
            mm = MyModel.objects.create(name=name)
            mm.save()
            return HttpResponseRedirect('/add') # Redirect after POST
    else:
        form = MyModelForm()
        args = {}
        args['form'] = form
    return render(request, 'main.html', args)

def form_add(request):
    args = {}
    name = request.session['name']
    args['name'] = name

    return render(request, 'add.html', args)
