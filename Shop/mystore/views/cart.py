from django.shortcuts import render
from mystore.models.products import Products
from mystore.models.customer import Customer
from mystore.models.orders import Orders
import datetime

def place_order(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        customer_id = request.POST.get('customer_id')
        quantity = int(request.POST.get('quantity'))

        product = Products.objects.get(id=product_id)
        customer = Customer.objects.get(id=customer_id)

        order = Orders(product=product, customer=customer, quantity=quantity, price=product.price)
        order.save()

        return render(request, 'order_placed.html', {'order': order})
    else:
        return render(request, 'error.html', {'message': 'Invalid request'})

def get_orders_by_customer(request, customer_id):
    orders = Orders.objects.filter(customer=customer_id).order_by('-date')
    return render(request, 'customer_orders.html', {'orders': orders})