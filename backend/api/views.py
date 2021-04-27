from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginUserSerializer, GFGSerializer
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from scripts.gfg_data import getGFGDetails


class RegisterUser(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GFGData(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        serializer = GFGSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            data = getGFGDetails(data['username'])

            if 'error' not in data:
                return Response({'data': data}, status=status.HTTP_200_OK)
            else:
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Please Enter a Username"}, status=status.HTTP_400_BAD_REQUEST)
