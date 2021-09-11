from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format= None):
        """Returns a list of API features"""
        an_apiview= [
            'uses HTTP methods as function(get, post, patch, put, delete)',
            'is similar to a traditional django view',
            'most control over logic',
            'mapped manually to urls'
        ]
        return Response({'message':"hello", 'an_apiview':an_apiview})
