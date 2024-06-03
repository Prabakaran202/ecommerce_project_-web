from django.urls import path
from .views import (
    wishlistAddView,
    wishlistListView,
    wishlistRemoveView
)

urlpatterns=[
    path('products/<str:id>/add_to_wishlist',wishlistAddView.as_view(),name='add-to-wishlist'),
    path('wishlist',wishlistListView.as_view(),name='wishlist'),
    path('wishlist/<str:id>',wishlistRemoveView.as_view(),name='wishlist-item-remove')
]