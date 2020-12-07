from rest_framework.routers import SimpleRouter

from spotify import views

app_name = 'spotify'

router = SimpleRouter()
router.register(
    prefix=r'',
    basename='spotify',
    viewset=views.SpotifyViewSet
)
urlpatterns = router.urls