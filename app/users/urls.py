from django.urls import path

from users.views import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

app_name = "users"
urlpatterns = [
    path('', login_required(UserList.as_view()), name='user_list'),
    path('delete/<int:pk>/',  login_required(DeleteUser.as_view()), name='delete_user'),
    path('create', login_required(UserCreate.as_view(success_url=reverse_lazy('users:user_list'))), name='create'),#todo
    path('edit1/<int:pk>/', login_required(UserEditMain.as_view()), name='user_edit1'),
    path('edit2/<int:pk>/<int:year>', login_required(PersonWorkTime.as_view()), name='user_edit2'),
    path('delete_work_time/<int:pk>', login_required(delete_work_time), name='delete_work_time'),
]
