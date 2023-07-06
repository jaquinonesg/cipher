'''
Tutorial source https://www.youtube.com/watch?v=c708Nf0cHrs

If I want to use raw model information and check it in the script or stuff
around the request, the information about that can be found around minute 50.
'''
from rest_framework import generics

from .models import User
from .serializers import UserSerializerCreate, UserSerializerDetail


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerCreate

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerDetail