"""
Like submission with options for successful and unsuccessful attempts
"""

from rest_framework.views import APIView
from rest_framework.response import Response


class SuccessfulLike(APIView):

    def post(self, request):
        """
        SuccessfulLike
        :param request: dict
        :return: json
        """
        data_response = dict()
        data_response["status"] = "ok"

        return Response(data_response)


class FailLike(APIView):

    def post(self, request):
        """
        FailLike
        :param request: dict
        :return: json
        """
        data_response = dict()
        data_response["status"] = "false"

        return Response(data_response)
