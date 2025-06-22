#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    # path('booking',views.bookingview.as_view(),name='booking'),
    # path('menu',views.menuview.as_view(),name='menu'),
    path('booking',views.BookingViewSet.as_view({'get': 'list'}),name='booking'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('user/',views.UserViewSet.as_view({'get': 'list'}),name='user'),
    path('message',views.msg),
    path('api-token-auth/', obtain_auth_token),
]
