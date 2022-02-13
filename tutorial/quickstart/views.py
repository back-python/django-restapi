from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from tutorial.quickstart.serializer import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow user to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = GroupSerializer
    permissions_classes = [permissions.IsAuthenticated]
