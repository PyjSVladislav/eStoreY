from django.http import response
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from .basket import Basket
from store.models import Product

# Create your views here.
def basket_summary(request):
    return render(request, 'store/basket/summary.html')

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        prodict_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id = product_id)
        basket.add(product=product, qty = prodict_qty)
        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)
        response = JsonResponse({'Success': True})
        return response