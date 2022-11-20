from django.urls import path
from django.views.decorators.cache import never_cache

from . import views

urlpatterns = [
    path('', views.StartPageView.as_view()),
    path('item/<int:pk>/', never_cache(views.ItemPageView.as_view()), name="item"),
    path('buy/<int:pk>/', views.create_checkout_session, name="buy"),
    path('config/', views.stripe_config),
    path('success/', views.SuccessPageView.as_view()),
    path('cancel/', views.CancelPageView.as_view())
]
