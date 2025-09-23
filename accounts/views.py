from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm, ProfileForm 
from django.contrib.auth import login
from django.contrib import messages
from django.db import transaction

class RegisterView(View):
    def get(self, request):
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
        show_captcha = request.session.get('failed_reg', 0) >= 1
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'show_captcha': show_captcha
        }
        return render(request, template_name='register.html', context=context)

    def post(self, request):
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        show_captcha = request.session.get('failed_reg', 0) >= 1

        if show_captcha and not request.POST.get('captcha', '').strip():
            messages.error(request, 'Пожалуйста, заполните капчу.')
            context = {'user_form': user_form, 'profile_form': profile_form, 'show_captcha': show_captcha}
            return render(request, template_name='register.html', context=context)

        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user  
                profile.save()

            login(request, user)
            request.session['failed_reg'] = 0
            return redirect('/')
        else:
            request.session['failed_reg'] = request.session.get('failed_reg', 0) + 1
            messages.error(request, 'Ошибка регистрации. Проверьте поля.')
            context = {'user_form': user_form, 'profile_form': profile_form, 'show_captcha': show_captcha}
            return render(request, template_name='register.html', context=context)