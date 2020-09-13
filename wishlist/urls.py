from django.urls import path

from .views import WishObjectListView, WishObjectDetailView, WishlistListView, WishlistDetailView

urlpatterns = [
    path('<int:fk>/wishObjects/<int:pk>', WishObjectDetailView.as_view()),
    path('<int:fk>/wishObjects/', WishObjectListView.as_view()),
    path('', WishlistListView.as_view()),
    path('<int:pk>', WishlistDetailView.as_view()),
]
