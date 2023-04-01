from django.http import HttpResponse

class XRobotsTagMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        """
        Code to be executed for each request before the view (and later
        middleware) are called.
        
        """
        
      
        
            

        
        
        
        
        '''
        do not delete below line. write anything before to call before view call
        '''    
        response = self.get_response(request) 
        response['X-Robots-Tag'] = 'noindex, nofollow'
        
        # Code to be executed for each request/response after
        # the view is called.
        return response
        
        
