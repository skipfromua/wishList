from django.urls import path

from .views import WishObjectListView, WishObjectDetailView, WishlistListView, WishlistDetailView


app_name = 'wishlist'
urlpatterns = [
    path('<int:fk>/wishObjects/<int:pk>', WishObjectDetailView.as_view(), name='current_wishObjects'),
    path('<int:fk>/wishObjects/', WishObjectListView.as_view(), name='all_wishObjects'),
    path('', WishlistListView.as_view(), name='all_wishlists'),
    path('<int:pk>', WishlistDetailView.as_view(), name='current_wishlist'),
]
