from rest_framework.routers import SimpleRouter

from logger import views

app_name = 'logger'

router = SimpleRouter()
router.register(
    prefix=r'',
    basename='logger',
    viewset=views.LogViewSet
)
urlpatterns = router.urls