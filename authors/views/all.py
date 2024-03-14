from django.http import Http404
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from cars.models import Cars
from django.urls import reverse

from authors.forms import RegisterForm, LoginForm


def authors_register(request):
    request_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(request_form_data)
    return render(request, 'authors/pages/authors_register.html', context={
        'forms': form,
        'form_action': reverse('authors:create')
    })


def authors_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, "your user has been created")
        del (request.session['register_form_data'])
        return redirect(reverse('authors:login'))

    return redirect('authors:register')


def authors_login(request):
    form = LoginForm()
    return render(request, 'authors/pages/authors_login.html', context={
        'forms': form,
        'form_action': reverse('authors:validation')
    })


def authors_login_validation(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'you are logged in')
            login(request, authenticated_user)
            return redirect('authors:dashboard')
        else:
            messages.error(request, 'invalidation credentials')
            return redirect('authors:login')
    else:
        messages.error(request, 'invalidation Username or Password')
        return redirect('authors:login')


@login_required(login_url='authors:login', redirect_field_name='next')
def authors_logout(request):
    if not request.POST:
        messages.error(request, "Invalid logout request")
        return redirect(reverse('authors:login'))

    if request.POST.get('username') != request.user.username:
        messages.error(request, "Invalid logout user")
        return redirect(reverse('authors:login'))

    logout(request)
    messages.success(request, "logout user successfuly")
    return redirect(reverse('authors:login'))


@login_required(login_url='authors:login', redirect_field_name='next')
def authors_dashboard(request):
    cars = Cars.objects.filter(is_published=False, author=request.user)
    return render(request, 'authors/pages/authors_dashboard.html', context={"cars": cars})
