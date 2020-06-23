from django.http import HttpResponse

class ErrorMessageMiddleware(object):
	def __init__(self,get_response):
		self.get_response=get_response

	def __call__(self, request):
		response= self.get_response(request)
		return response

	def process_exception(self,exception,request):
		msg= '<h1> Currently we are facing some technical issue..Please come back after sometime</h1>'
		return HttpResponse(msg)