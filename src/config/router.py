from core.nexus_inventory import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'categories', views.CategoryViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'asset-history', views.AssetHistoryViewSet)
