"""
Request data about tasks for bot
"""

from rest_framework.views import APIView
from rest_framework.response import Response


class GetTasks(APIView):

    def get(self, request, *args, **kwargs):
        """
        GetTasks for bot
        :param request:
        :return: json
        """
        print(request)
        data_response = dict()
        data_response["status"] = "ok"
        data_response["bot_id"] = kwargs["id"]
        data_response["tasks"] = {"one": "login", "two": "Set like"}

        return Response(data_response, headers={'Cache-Control': 'no-cache'})