from django.http import Http404
from django.contrib import messages
from django.shortcuts import redirect, render

from authors.forms import RegisterModel


def authors_register(request):
    request_form_data = request.session.get('register_form_data', None)
    form = RegisterModel(request_form_data)
    return render(request, 'authors/pages/authors_register.html', context={
        'forms': form,
    })


def authors_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterModel(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, "your user has been created")
        del (request.session['register_form_data'])

    return redirect('authors:register')
