from django.urls import path
from .views import RegisterUserView, LoginUserView, GetUsersView, GFGDataView, GetAndUpdateUserView, UpdateDataView, LeetcodeDataView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name="register_user"),
    path('login/', LoginUserView.as_view(), name="login_user"),
    path('users/', GetUsersView.as_view(), name="get_all_users"),
    path('user/', GetAndUpdateUserView.as_view(), name="get_and_update_user"),
    path('gfg/', GFGDataView.as_view(), name="gfg_data"),
    path('leetcode/', LeetcodeDataView.as_view(), name="leetcode_data"),
    path('update/', UpdateDataView.as_view(), name="update_data"),
]
