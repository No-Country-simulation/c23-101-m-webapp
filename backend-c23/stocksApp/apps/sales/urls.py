from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'sales', SaleViewSet, basename='sales')

urlpatterns = [
    path('', include(router.urls)),
    path('profit-reports/', ProfitReportViewSet.as_view({'get': 'list'}), name='profit-reports'),
    path('profit-reports/<int:pk>/update/', ProfitReportViewSet.as_view({'get': 'update'}), name='profit-report-update'),
]