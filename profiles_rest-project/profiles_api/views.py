from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format= None):
        """Returns a list of API features"""
        an_apiview= [
            'uses HTTP methods as function(get, post, patch, put, delete)',
            'is similar to a traditional django view',
            'most control over logic',
            'mapped manually to urls'
        ]
        return Response({'message':"hello", 'an_apiview':an_apiview})

    def post(self, request, format=None):
        """Create a hello massayge with our name"""
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status =status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk= None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk= None):
        """Handle partial updating an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk= None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
        



