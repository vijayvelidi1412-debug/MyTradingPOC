"""
URL configuration for the project
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.users.views import AuthViewSet, UserViewSet, UserProfileViewSet, CashCreditViewSet
from apps.trading.views import ContractViewSet, TradeViewSet, PositionViewSet, PriceHistoryViewSet
from apps.settlements.views import SettlementViewSet, CreditNoteViewSet, RolloverViewSet

# Create router and register viewsets
router = DefaultRouter()

# Auth and User endpoints
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'users', UserViewSet, basename='user')
router.register(r'profiles', UserProfileViewSet, basename='profile')
router.register(r'cash-credits', CashCreditViewSet, basename='cash-credit')

# Trading endpoints
router.register(r'contracts', ContractViewSet, basename='contract')
router.register(r'trades', TradeViewSet, basename='trade')
router.register(r'positions', PositionViewSet, basename='position')
router.register(r'price-history', PriceHistoryViewSet, basename='price-history')

# Settlement endpoints
router.register(r'settlements', SettlementViewSet, basename='settlement')
router.register(r'credit-notes', CreditNoteViewSet, basename='credit-note')
router.register(r'rollovers', RolloverViewSet, basename='rollover')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
