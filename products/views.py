from rest_framework import views, exceptions, response
from .models import Product
from .serializers import ProductSerializer


class ProductsBehaviour(views.APIView):
    def post(self, request):
        if Product.objects.filter(barCode=request.data['code']).exists():
            serializer = ProductSerializer(Product.objects.filter(barCode=request.data['code']).first())
            return response.Response(serializer.data, 200)

        print(request.data)
        raise exceptions.NotFound('Code not found.')
