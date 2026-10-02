from django.shortcuts import render
from .serializers import ProductSerializer,CartReadSerializer,CartWriteSerializer
from .models import Product,Cart
from rest_framework import generics, status
from rest_framework.response import Response

# Cnreate your views here.

# drf provide a class based view not a function

# this class for list and post products

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# this class for get put delete products

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer



   


class CartUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    def get_serializer_class(self):
        if self.request.method == "GET":
            return CartReadSerializer
        return CartWriteSerializer

    
class CartListCreate(generics.ListCreateAPIView):
    queryset = Cart.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CartReadSerializer
        return CartWriteSerializer

    def post(self, request, *args, **kwargs):

        product_id = request.data.get("product")
        quantity = int(request.data.get("quantity", 1))

        print("Product ID:", product_id)   # Debug

        try:
            cart_item = Cart.objects.get(product_id=product_id)

            cart_item.quantity += quantity
            cart_item.save()

            serializer = CartReadSerializer(cart_item)
            return Response(serializer.data)

        except Cart.DoesNotExist:

            serializer = CartWriteSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()

                read_serializer = CartReadSerializer(serializer.instance)
                return Response(read_serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



