from rest_framework.views import APIView
from rest_framework.response import  Response


class HomeView(APIView):


    def get(self, request):
        content = {
            'message': 'Hello world'
        }
        return Response(content)
