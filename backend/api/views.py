from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from scripts.gfg_data import getGFGDetails
from scripts.leetcode_data import getLeetcodeData
from .models import User, GFGData, LeetcodeData
from .serializers import (RegisterUserSerializer, LoginUserSerializer,
                          GFGDataSerializer, LeetcodeDataSerializer)
from .utils import (TokenUtils,
                    send_email_on_user_creation, send_email_on_user_creation_leetcode,
                    updateGFGData, updateLeetcodeData, process_tasks)


class RegisterUserView(APIView):
    @staticmethod
    def post(request):
        serializer = RegisterUserSerializer(data=request.data)
        # noinspection PyBroadException
        try:
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                token = str(RefreshToken.for_user(user).access_token)
                return Response({**serializer.data, 'token': token}, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(APIView):
    @staticmethod
    def post(request):
        serializer = LoginUserSerializer(data=request.data)
        print(serializer)
        # noinspection PyBroadException
        try:
            if serializer.is_valid(raise_exception=True):
                user = User.objects.get(id=serializer.data['id'])
                token = str(RefreshToken.for_user(user).access_token)
                return Response({**serializer.data, 'token': token}, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAndUpdateUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = TokenUtils.get_user_from_token(self, request)
        serializer = RegisterUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        user = TokenUtils.get_user_from_token(self, request)
        serializer = RegisterUserSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUsersView(APIView):
    permission_classes = [permissions.IsAdminUser, ]

    @staticmethod
    def get(request):
        qs = User.objects.all()
        if not qs:
            return Response({'error': 'No users were found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = RegisterUserSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GFGDataView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # GET USER MODEL FROM TOKEN
        user = TokenUtils.get_user_from_token(self, request)

        if not user.handle_verified:
            return Response({'error': ['Please Enter your handle/username first']}, status=status.HTTP_401_UNAUTHORIZED)

        gfg_data = GFGData.objects.get(user=user.id)
        serializer = GFGDataSerializer(gfg_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # GET USER MODEL FROM TOKEN
        user = TokenUtils.get_user_from_token(self, request)

        # CHECK IF GFGDATA FOR USER ALREADY EXISTS
        handle = request.data['gfg_handle']

        # noinspection PyBroadException
        try:
            handleData = GFGData.objects.get(user=user.id, gfg_handle=handle)
            if handleData:
                return Response({'error': ["User data already Exists"]}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        # GET GFG DATA FROM SCRIPT
        script_data = getGFGDetails(request.data['gfg_handle'])
        if 'error' in script_data:
            return Response({'error': 'Something went Wrong', 'msg': script_data['error']},
                            status=status.HTTP_400_BAD_REQUEST)

        # SERIALIZERS
        serializer = RegisterUserSerializer(instance=user, data={'handle_verified': True, 'is_gfg': True}, partial=True)
        serializer1 = GFGDataSerializer(data={'user': user.id, **script_data, 'gfg_handle': handle})

        if serializer.is_valid(raise_exception=True) and serializer1.is_valid(raise_exception=True):
            serializer1.save()
            serializer.save()
            send_email_on_user_creation({**serializer.data, **serializer1.data})

            return Response({'data': serializer1.data}, status=status.HTTP_200_OK)
        return Response({**serializer.errors, **serializer1.errors}, status=status.HTTP_200_OK)


class LeetcodeDataView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # GET USER MODEL FROM TOKEN
        user = TokenUtils.get_user_from_token(self, request)

        # CHECK IF LEETCODE DATA FOR USER ALREADY EXISTS
        handle = request.data['leetcode_handle']

        # noinspection PyBroadException
        try:
            handleData = LeetcodeData.objects.get(user=user.id, leetcode_handle=handle)
            if handleData:
                return Response({'error': "User already Exists"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

            # GET LEETCODE DATA FROM SCRIPT
            script_data = getLeetcodeData(request.data['leetcode_handle'])
            if 'error' in script_data:
                return Response(script_data, status=status.HTTP_400_BAD_REQUEST)

            # SERIALIZERS
            serializer = RegisterUserSerializer(instance=user, data={'handle_verified': True}, partial=True)
            serializer1 = LeetcodeDataSerializer(data={'user': user.id, **script_data, 'leetcode_handle': handle})

            if serializer.is_valid(raise_exception=True) and serializer1.is_valid(raise_exception=True):
                serializer1.save()
                serializer.save()
                send_email_on_user_creation_leetcode({**serializer.data, **serializer1.data})

                return Response({'data': serializer1.data}, status=status.HTTP_200_OK)
            return Response({**serializer.errors, **serializer1.errors}, status=status.HTTP_200_OK)


class UpdateDataView(APIView):
    @staticmethod
    def get(request):
        queryset = User.objects.all()
        serializer = RegisterUserSerializer(queryset, many=True)

        updateGFGData(serializer.data)
        updateLeetcodeData(serializer.data)

        process_tasks()

        return Response({'data': 'Sending Email'}, status=status.HTTP_200_OK)
