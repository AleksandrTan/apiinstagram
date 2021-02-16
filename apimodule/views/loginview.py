"""
Login submission with options for successful and unsuccessful attempts
"""

from rest_framework.views import APIView
from rest_framework.response import Response


class SuccessfulLogin(APIView):

    def post(self, request):
        """
        SuccessfulLogin
        :param request: dict
        :return: json
        """
        data_response = dict()
        data_response["status"] = "ok"
        data_response["email"] = request.data.get("email", False)
        data_response["password"] = request.data.get("password", False)

        return Response(data_response)


class FailLogin(APIView):

    def post(self, request):
        """
        FailLogin
        :param request: dict
        :return: json
        """
        data_response = dict()
        data_response["status"] = "false"

        return Response(data_response)
