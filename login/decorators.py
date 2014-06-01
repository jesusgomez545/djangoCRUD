from django.template import RequestContext
from django.http import HttpResponse ,HttpResponseRedirect

def loginRequired(view):
	def wrapper(request):
		try:	
			if not request.session.has_key('has_loged'):
				return HttpResponseRedirect('/')
			else:
				raise	
		except Exception, e:
			return view(request)			
	return wrapper



def alreadyLoged(view):
	def wrapper(request):
		try:
			if request.session.has_key('has_loged'):
				return HttpResponseRedirect('/home')
			else:
				raise	
		except Exception, e:
			return view(request)			
	return wrapper