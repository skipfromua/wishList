from django.urls import path

from .views import WishObjectListView, WishObjectDetailView, WishlistListView, WishlistDetailView, WishObjectReserveView


app_name = 'wishlist'
urlpatterns = [
    path('reserve/<int:to_wishlist_id>', WishObjectReserveView, name='reserve'),
    path('<int:fk>/wishObjects/<int:pk>', WishObjectDetailView.as_view(), name='current_wishObject'),
    path('<int:fk>/wishObjects/', WishObjectListView.as_view(), name='all_wishObjects'),
    path('', WishlistListView.as_view(), name='all_wishlists'),
    path('<int:pk>', WishlistDetailView.as_view(), name='current_wishlist'),
]
