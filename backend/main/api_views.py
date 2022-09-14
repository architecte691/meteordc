import email
import json
from django.urls import reverse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from connect.models import User, Post, PostImage


class Profil(APIView):
    permission_classes = [IsAuthenticated]
    parser_class = (FileUploadParser, FormParser, MultiPartParser)

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

    def post(self, request, format='json'):
        print('--------------((____________(((api))____________))))(------------')
        user = User.objects.get(id=request.user.id)
        data = request.data
        print(user)
        print(data)
        for name, value in data.items():
            if name in ['email', 'username', 'first_name', 'last_name', 'country', 'city', 'new_avatar']:
                if name == 'new_avatar':
                    print('file in data _________')
                    print(value)
                    user.avatar.save(value.name, value, save=True)
                else:
                    vars(user)[name] = value
                user.save()

        res = {}
        res['auth'] = str(request.auth)
        return Response(res)


class PostView(APIView):
    permission_classes = (IsAuthenticated, )
    parser_class = (FileUploadParser, FormParser, MultiPartParser)

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

    def post(self, request, hospital_id, patient_id, fiche_id, voucher_id, format='json'):
        print('--------------((____________(((api))____________))))(------------')
        user = User.objects.get(id=request.user.id)
        data = request.data
        print(user)
        print(data)

        post = Post.objects.create(
            editor_id=user.id, type=data['type'], description=data['description'])
        print('files in data _________')
        if data.get('images_id'):
            for name, value in data.items():
                if 'image-' in name:
                    print(name)
                    print(data.get(name))
                    img = PostImage(editor_id=user.id, post=post)
                    img.file.save(data.get(name).name,
                                  data.get(name), save=True)
                    img.save()
        post.save()

        res = {
            'id': post.id,
            'editor': {
                'id': post.editor.id,
                'name': post.editor.username,
                'avatar': post.editor.avatar.url if post.editor.avatar else ''
            } if post.editor else None,
            'type': post.type,
            'description': post.description,
            'date': str(post.date),
            'images': [
                {'id': img.id, 'url': img.file and img.file.url}
                for img in post.post_images.all()
            ],
            'data': post.data
        }
        return Response(res)


class Register(APIView):
    permission_classes = [AllowAny]
    parser_class = (FileUploadParser, FormParser, MultiPartParser)

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

    def post(self, request, format='json'):
        print(
            '--------------((____________(((api create user))____________))))(------------')
        data = request.data
        user = User.objects.create(
            email=data['email'],
            password=data['password'],
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )
        print(user)
        print(data)
        user.save()

        token = {}
        refresh = RefreshToken.for_user(user)
        token['refresh'] = str(refresh)
        token['access'] = str(refresh.access_token)

        content = {
            'user': str(user),  # `django.contrib.auth.User` instance.
            'auth': token,  # None
        }
        print(content)
        return Response(content)
