from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from user.serializers import CustomAuthTokenSerializer, UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Створення нового користувача в системі."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Створення нового токена автентифікації для користувача
    за допомогою кастомного серіалізатора."""
    serializer_class = CustomAuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Управління профілем автентифікованого користувача."""
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        """Повертає об'єкт поточного автентифікованого користувача."""
        return self.request.user
