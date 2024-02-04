from typing import List
from rest_framework.views import APIView
from rest_framework.response import Response

from shuffle.functions import python_shuffle
# Create your views here.
class Shuffler(APIView):
    def post(self, request):
        input: List[any] = request.data["input"]
        output = python_shuffle(input)
        return Response(output)
