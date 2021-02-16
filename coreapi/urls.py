from django.urls import path
from coreapi.views.gettask import GetTasks
from coreapi.views.setlog import SetLogs

urlpatterns = [
    path('bot/<int:id>/tasks/', GetTasks.as_view(), name="get_task"),
    path('bot/<int:id>/setlog/', SetLogs.as_view(), name="set_logs")
]