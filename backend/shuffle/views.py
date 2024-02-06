from typing import List
from rest_framework.views import APIView
from rest_framework.response import Response

from shuffle.functions import final_shuffle, python_shuffle
# Create your views here.
class Shuffler(APIView):
    def post(self, request):
        input: List[any] = request.data["input"]
        response = {'data': final_shuffle(input)}
        return Response(response)
