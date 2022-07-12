from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth for user. renderer class sets the renderer
     so we can view this endpoint in the browser with browsable api i.e. POST instead
     of curl"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
