from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class SecretView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        data = {"message": "Secret text."}
        return Response(data)
