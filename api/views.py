import stripe
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView
from rest_framework import status
from rest_framework.response import Response

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def stripe_config(request):
    """Получение sessionID по запросу на /buy/{item_id}"""
    if request.method == 'GET':
        config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(config, safe=False)


@csrf_exempt
def create_checkout_session(request, pk):
    """
    Страница создания checkout сессии после покупки товара
    """
    item = _get_item_object(pk)
    if request.method == 'GET':
        base_url = f'http://{request.get_host()}'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=base_url + '/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=base_url + '/cancel/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name
                        }
                    },
                    'quantity': 1
                }])
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class ItemPageView(DetailView):
    """Страница с информацией о товаре"""
    template_name = 'itemdetail.html'
    model = Item


class SuccessPageView(TemplateView):
    """Страница с информацией об успешной транзакции"""
    template_name = 'success.html'


class CancelPageView(TemplateView):
    """Страница с информацией об отменной транзакции"""
    template_name = 'cancel.html'


class StartPageView(TemplateView):
    """Стартовая страница"""
    template_name = 'hello.html'


def _get_item_object(pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response("Товар не найдет",
                        status=status.HTTP_404_NOT_FOUND)

    return item
