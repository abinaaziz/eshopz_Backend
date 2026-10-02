from django.urls import path
from .views import ProductDetailView, ProductListCreateView,CartListCreate,CartUpdateDelete


urlpatterns= [
    path('Product',ProductListCreateView.as_view(),name='Product-list-create'),
    path('Product/<int:pk>',ProductDetailView.as_view(),name='Product-detail'),
    path("Cart/", CartListCreate.as_view(),name='Cart-list-create'),
    path("Cart/<int:pk>/", CartUpdateDelete.as_view(),name='Cart-update-delete'),

]