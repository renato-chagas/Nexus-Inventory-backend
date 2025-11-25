from rest_framework.routers import DefaultRouter

from core.nexus_inventory import views as inventory_views
from core.usuario.router import router as usuario_router
from core.uploader.router import router as uploader_router

router = DefaultRouter()

router.register(r"categories", inventory_views.CategoryViewSet)
router.register(r"employees", inventory_views.EmployeeViewSet)
router.register(r"assets", inventory_views.AssetViewSet)
router.register(r"asset-history", inventory_views.AssetHistoryViewSet)
router.register(r"softwares", inventory_views.SoftwareViewSet)

# Agrega as rotas dos apps usuario e uploader ao router principal
router.registry.extend(usuario_router.registry)
router.registry.extend(uploader_router.registry)
