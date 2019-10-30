from django.contrib.auth import get_user_model
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from pastebin.users.permissions import IsAuthenticatedOrCreate
from pastebin.users.serializers import UserSerializer

User = get_user_model()


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
    http_method_names = ['get', 'post', 'head', 'put']
    permission_classes = [IsAuthenticatedOrCreate]
