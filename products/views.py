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


class AddProduct(views.APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        newProduct = Product(**serializer.data)
        newProduct.save()

        return response.Response(serializer.data, 201)
