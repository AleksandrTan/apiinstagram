"""
Set log records about bots work
"""

from rest_framework.views import APIView
from rest_framework.response import Response


class SetLogs(APIView):

    def post(self, request, *args, **kwargs):
        """
        SetLogs for bot
        :param request:
        :return: json
        """
        print(request.data)
        data_response = dict()
        data_response["status"] = "ok"

        return Response(data_response, headers={'Cache-Control': 'no-cache'})