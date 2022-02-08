import json
from rest_framework.views import APIView
from django.http import HttpResponse
from .serializers import DecryptMessageSerializer


class DecryptMessageAPI(APIView):
    def post(self, request):
        data = DecryptMessageSerializer(data=request.data)
        if data.is_valid():
            return HttpResponse(
                    json.dumps({"DecryptedMessage": f"{data.message} decrypted using GPG {data.passphrase}"}),
                    content_type="application/json",
                )