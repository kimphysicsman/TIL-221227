
from django.urls import path

from user.views import UserView

# user/
urlpatterns = [
    path("", UserView.as_view(), name="user"),
]