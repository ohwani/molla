from django.shortcuts import render
from django.http import JsonResponse

# from rest_framework.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions, authentication
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer

from .models import User

# Create your views here.

'''viewset 이용 '''

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [IsAuthenticated]
    # authentication_classes = (JWTAuthentication)


# class UserLoginView(views.APIView):
#     permission_classes = (permissions.AllowAny)
#     authentication_classes = (CsrfExemptSessionAuthentication)

#     def post(self, request):
#         serializer = LoginSerializer(data = request.data)
#         serializer.is_valid()



# class LoginViewSet(viewsets.ModelViewSet):

#     queryset = User.objects.all()










































# class ReviewCreateAPIView()

'''FBV api_view decorator 이용'''
# @api_view(['GET', 'POST'])
# def userList(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def userDetail(request, pk):
#     if request.method == 'GET':
#         user = User.objects.get(id=pk)
#         serializer = UserSerializer(user, many=False)
#         return Response(serializer.data)

#     elif request.method == 'PATCH':
#         user = User.objects.get(id=pk)
#         serializer = UserSerializer(instance=user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#     else:
#         user = User.objects.get(id=pk)
#         user.delete()
#         return Response(serializer.data, status=204)

# '''generics.py + mixin''' 

# class UserListMixins(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetailMixins(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


'''CBV apiview'''

# class UserListAPIView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#         return Response(serializer.data)

# class UserDetailAPIView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(User, pk=pk)

#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = USerSerializer(user)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
