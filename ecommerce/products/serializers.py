from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# order
class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset = Product.objects.all()
    )
    product_name = serializers.CharField(source = "product.name", read_only = True)

    class Meta:
        model = OrderItem
        fields = ['product','product_name','quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many = True)

    class Meta:
        model = Order
        fields = ['address','contact_no','email','payment_method','status','items','id','created_at','total_price']


    def create(self,validated_data):
        items_data = validated_data.pop('items')    

        user = self.context['request'].user

        order = Order.objects.create(
           user = user,
           **validated_data
        )

        for item_data in items_data:
            product = item_data['product'] # send product id from frontend
            price = product.price
            quantity = item_data['quantity']

            OrderItem.objects.create(
                order = order,
                product = product,
                price = price,
                quantity = quantity
            )

        order.calculate_total()

        order.save()

        return order    
