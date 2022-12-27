from django.contrib import auth

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserView(APIView):
    def post(self, request):
        user = auth.authenticate(request, **request.data)
        if not user:
            return Response({"message": "로그인에 실패했습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        auth.login(request, user)
        return Response({"message": "로그인에 성공했습니다."}, status=status.HTTP_200_OK)