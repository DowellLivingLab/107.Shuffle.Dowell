from typing import List
from rest_framework.views import APIView
from rest_framework.response import Response

from shuffle.functions import final_shuffle, python_shuffle

# views.py
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
# Create your views here.
class Shuffler(APIView):
    def post(self, request):
        print(request.data)
        input: List[any] = request.data["input"]
        response = {'data': final_shuffle(input)}
        print(response)
        return Response(response)

