from django.http import Http404
from django.shortcuts import redirect, render

from authors.forms import RegisterModel


def authors_register(request):
    request_form_data = request.session.get('request_form_data', None)
    form = RegisterModel(request_form_data)
    return render(request, 'authors/pages/authors_register.html', context={
        'forms': form,
    })


def authors_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['request_form_data'] = POST
    form = RegisterModel(request.POST)
    return redirect('authors:register')
