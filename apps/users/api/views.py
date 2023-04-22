from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework import renderers

from users.api.serializers import UserSerializer, GroupSerializer
from users.models import User

from django.contrib.auth.views import LoginView


# Create your views here.
class CustomRenderer(renderers.BaseRenderer):
    media_type = 'image/png'
    format = 'png'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data


class TestView(APIView):
    # renderer_classes = (CustomRenderer,)

    def get(self, request, *args, **kwargs):
        url = request.META.get('HTTP_REFERER')
        if not url:
            img = ''
            return Response(data=request.user.username, content_type='*/*')
        else:
            return Response({'current_site': url}, status=status.HTTP_403_FORBIDDEN)


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# @csrf_exempt
class UserLoginCustomView(LoginView):
    pass
