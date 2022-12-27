from django.contrib.auth.backends import BaseBackend
from user.models import User as UserModel

class CustomBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = UserModel.objects.get(username=username, password=password)
        except UserModel.DoesNotExist:
           return None
        return user

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None