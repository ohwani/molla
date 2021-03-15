from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

from .models import User
# Create your views here.


@api_view(['GET'])
def accountsOverview(request):
    api_urls = {
        'id': 1,
        'username': 'ohwani',
        'password': 12341234,
        'emali': '1234@naver.com'
    }

    return Response(api_urls)


@api_view(['GET'])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def userDetail(request, pk):
    if request.method == 'GET':
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    else:
        user = User.objects.get(id=pk)
        user.delete()
        return Response(serializer.data, status=204)


# @api_view(['GET'])
# def userDetail(request, pk):
#     user = User.objects.get(id=pk)
#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)

# @api_view(['PATCH'])
# def userUpdate(request, pk):
#     user = User.objects.get(id=pk)

#     serializer = UserSerializer(instance=user, data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def userDelete(request):
#     user = User.objects.get(id=pk)
#     user.delete()

#     return Response(serializer.data)


# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import User
# from .serializers import UserSerializer


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
