# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, permissions, authentication
# from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import (
    UserSerializer,
)

from .models import User

# class UserRegisterationView(APIView):
#     serializer_class = UserRegisterSerializer
#     # permission_classes = (AllowAny)

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         vaild = serializer.is_valid(rasie_exception=True)

#         if valid:
#             serializer.save()
#             status_code = status.HTTP_201_CREATED

#             response = {
#                 'success': True,
#                 'statusCode': status_code,
#                 'message': 'User successfully registered!',
#                 'user': serializer.data
#             }

#             return Response(response, status=status_code)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [AllowAny]

    # @action(detail=False)
    # def create(self, request, *args, **kwargs):
    #     '''
    #     사용자 등록
    #     '''
    #     data = request.data

