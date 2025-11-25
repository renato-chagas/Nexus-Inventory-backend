from rest_framework.routers import DefaultRouter

from . import views

app_name = "user"

router = DefaultRouter()
router.register("users", views.UserViewSet)
