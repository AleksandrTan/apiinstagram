from django.urls import path
from apimodule.views.loginview import (SuccessfulLogin, FailLogin)
from apimodule.views.likeview import (SuccessfulLike, FailLike)

urlpatterns = [
    path('successlogin/', SuccessfulLogin.as_view(), name="success_login"),
    path('faillogin/', FailLogin.as_view(), name="fail_login"),
    path('successlike/', SuccessfulLike.as_view(), name="success_like"),
    path('faillike/', FailLike.as_view(), name="fail_like")
]
