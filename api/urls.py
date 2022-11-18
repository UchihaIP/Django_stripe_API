from django.urls import path

from . import views

urlpatterns = [
    path('item/<int:pk>/', views.ItemView.as_view()),
    path('buy/<int:pk>/', views.create_checkout_session, name="buy"),
    path('config/', views.stripe_config),
    path('success/', views.SuccessView.as_view()),
    path('cancel/', views.CancelView.as_view())
]
