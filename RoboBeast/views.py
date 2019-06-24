from django.contrib.auth import login as django_login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_auth.serializers import LoginSerializer
from rest_framework.authtoken.models import Token
# from django.core.context_processors import csrf
# from .forms import RegistrationForm
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import *

# Create your views here.


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["User"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponse("logout Succesfully")

# UserProfile


class UserProfileListAPIView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.filter(is_active=True)
    serializer_class = UserProfileSerializer
    lookup_field = 'user_id'


class UserProfileCreateAPIView(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

#
# def Form(request):
#     return render(request, "index/form.html", {})


# def Upload(request):
#     for count, x in enumerate(request.FILES.getlist("files")):
#         def process(f):
#             with open('DisplayImage' + str(count), 'wb+') as destination:
#                 for chunk in f.chunks():
#                     destination.write(chunk)
#         process(x)
#     return HttpResponse("File(s) uploaded!")