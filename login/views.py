from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse ,HttpResponseRedirect

from login.models import *
from login.decorators import *


"""
NOTE
====
	The start view needs to provide the entire context_instance
	because Django uses a security level called CSRF, that means 
	any froms which makes uses of the http POST method must include such 
	token on its body to permit the authentication run correctly
"""

""""
DISPATHCHERS
============
"""
@alreadyLoged
def start(request):
	return render_to_response('index.html',{'err':0 }, context_instance=RequestContext(request))

@loginRequired
def home(request):
	return render_to_response('home.html',{'usuarios': ManejadorUsuario.listarUsuarios()}, context_instance=RequestContext(request))

def error(request):
	return render_to_response('error.html', context_instance=RequestContext(request))


"""
CONTROLLERS
===========
"""
@alreadyLoged
def login(request):
	try:
		if request.method == 'POST' :
			if request.POST['login'] and request.POST['password']:
				if len(ManejadorUsuario.auntenticarUsuario(request.POST['login'], request.POST['password'])):				
					request.session['has_loged'] = True
					request.session['username'] = request.POST['login']
					return HttpResponseRedirect('/home')
				else:
					return render_to_response('index.html',{'err':1 }, context_instance=RequestContext(request))
			else:
				raise Exception("error")
		else :
			raise Exception("error")		
	except Exception, e:
		return render_to_response('index.html',{'err':2 }, context_instance=RequestContext(request))

@loginRequired	
def logout(request):
    try:
        request.session.flush()
    except KeyError:
		pass
    return HttpResponseRedirect('/')

@loginRequired
def editUser(request):
	try:
		if request.method == 'POST':
			try:
				if ManejadorUsuario.editarUsuario(request.POST['u'], request.POST['e']):
					return HttpResponse(status=200)
				else:
					raise Exception("error")				
			except Exception, e:
				return HttpResponse(status=403)
		else:
			raise Exception("error")
	except Exception, e:
		return HttpResponseRedirect('/error', status=403)	

@loginRequired
def deleteUser(request):
	try:
		if request.method == 'POST':
			if ManejadorUsuario.eliminarUsuario(request.POST['t'], request.session['username']):
				return HttpResponse(status=200)
			else:
				raise
		else:
			raise Exception("error")
	except Exception, e:
		return HttpResponseRedirect('/error', status=403)