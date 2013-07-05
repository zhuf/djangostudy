#-*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from django.conf import settings
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache

from django.template.response import TemplateResponse
from django.contrib.sites.models import get_current_site

from django.contrib.auth.models import User
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.http import base36_to_int, is_safe_url

from django.template import RequestContext 

from django.contrib import messages

import csv

from im.models import Stu, Fi
from im.forms import StuForm, FiForm, AuthenticationForm

@login_required
def lists(request):
	stus = Stu.objects.all().order_by('-id')
	fis = Fi.objects.all().order_by('-id')

	return render_to_response('list.html', locals())

@csrf_exempt
def upload(request):
	if request.method == 'POST':
		form = StuForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/lists')
	return HttpResponseForbidden('allowed only via POST')

@csrf_exempt
def upload_file(request):
	if request.method == 'POST':
		form = FiForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/lists')
	return HttpResponseForbidden('allowed only via POST')

@sensitive_post_parameters()
@csrf_protect
@never_cache
def login_view(request, template_name='registration/login.html',
				redirect_field_name=REDIRECT_FIELD_NAME,
				authentication_form=AuthenticationForm,
				current_app=None, extra_context=None):
	"""
		Displays the login form and handles the login action.
	"""
	redirect_to = request.REQUEST.get(redirect_field_name, '')

	if request.method == "POST":
		form = authentication_form(data=request.POST)

		if form.is_valid():

			if not is_safe_url(url=redirect_to, host=request.get_host()):
 				redirect_to = settings.LOGIN_REDIRECT_URL

			user = form.get_user()
			username = user.username
			password = user.password

			auth_login(request, user)

			if request.session.test_cookie_worked():
				request.session.delete_test_cookie()
			return HttpResponseRedirect(redirect_to)
	else:
		form = authentication_form(request)

	request.session.set_test_cookie()

	current_site = get_current_site(request)

	context = {
			'form': form,
			redirect_field_name: redirect_to,
			'site': current_site,
			'site_name': current_site.name,
	}
	if extra_context is not None:
		context.update(extra_context)
	return TemplateResponse(request, template_name, context, current_app=current_app)

def logout_view(request):
	auth_logout(request)
	return redirect('/accounts/login')

def profile_view(request):
	if request.method == 'POST':
		username = request.POST.get('username', '')
		name = request.POST.get('name', '')

		errors = []
		user = User.objects.get(username=username)

		used_name = user.first_name

		password = request.POST.get('password', '')
		confirm_password = request.POST.get('confirm_password', '')

		if used_name != name:
			user.first_name = name
			user.save()
			messages.success(request, 'Profile details updated.')

		if password != '' and password == confirm_password:
			messages.success(request, 'password updated.')
			user.set_password(password)
			user.save()
		elif password != confirm_password:
			messages.error(request, 'password error.')
		else:
			pass
	
		return HttpResponseRedirect('/accounts/profile/')
	return render_to_response('profile.html', {'request': request}, context_instance=RequestContext(request))

def generate_csv(request):
	response = HttpResponse(content_type="text/csv")
	response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

	writer = csv.writer(response)

	writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
	writer.writerow(['Second row', 'A', 'B', 'C', 'D'])

	return response

def display_meta(request):
	values = request.META.items()
	values.sort()

	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))