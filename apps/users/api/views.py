import json

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from oauth2_provider.signals import app_authorized
from oauth2_provider.views.base import TokenView
from oauth2_provider.models import AccessToken, Application, get_access_token_model
from oauthlib.common import generate_token
from rest_framework import renderers
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils import decrypt_image
from users.api.serializers import UserSerializer, GroupSerializer
from users.models import User


# Create your views here.
class CustomRenderer(renderers.BaseRenderer):
    media_type = 'image/jpeg'
    format = 'jpg'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data


class TestView(APIView):
    renderer_classes = (CustomRenderer,)

    def get(self, request, *args, **kwargs):
        url = request.META.get('HTTP_REFERER')
        # if not url:
        # img = ''
        a = User.objects.filter(email='a@a.com').first()
        # fin = open(a.avatar.path, 'rb')
        # file = fin.read()
        file = decrypt_image(a.avatar.path)

        return Response(data=file, content_type='*/*')
        # else:
        #     return Response({'current_site': url}, status=status.HTTP_403_FORBIDDEN)


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


class UserLoginCustomView(generics.GenericAPIView, TokenView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        url, headers, body, stat = self.create_token_response(request)
        if stat == 200:
            body = json.loads(body)
            access_token = body.get("access_token")
            if access_token is not None:
                token = get_access_token_model().objects.get(token=access_token)
                app_authorized.send(sender=self, request=request, token=token)
        body["user"] = UserSerializer(token.user, many=False).data
        response = Response(data=body, headers=headers, status=stat)
        return response


class UserRegisterCustomView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token = self.generate_token()
        return Response({"user": serializer.data, "access_token": str(token.token)}, status=status.HTTP_201_CREATED,
                        headers=headers)

    def perform_create(self, serializer):
        user = serializer.save()
        self.request.user = user

    def generate_token(self):
        application = Application.objects.first()
        token = generate_token()
        access_token = AccessToken.objects.create(user=self.request.user, application=application,
                                                  expires=timezone.now() + relativedelta(hours=24 * 30 * 12),
                                                  token=token, scope='user')
        return access_token
