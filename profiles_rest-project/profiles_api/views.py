from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from . import models
from . import serializers
from . import permissions


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



class HellloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class= serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""
        a_viewset = [
            'uses actions (list, create, retrieve, update, partial_update)',
            'automatically maps to URLs using Routers',
            'provides more functionality with less code',
        ]
        return Response({'message':'hello', 'a_viewset':a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """handle getting an object by its id"""
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
            """handle updating an object by its id"""
            return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handle updating part of an object by its id"""
        return Response({'http_method': 'PATCH'})
        
    def destroy(self, request, pk=None):
            """handle removing an object by its id"""
            return Response({'http_method': 'DELETE'})
    


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)



class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    