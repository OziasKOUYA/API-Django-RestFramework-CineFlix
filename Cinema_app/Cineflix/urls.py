from django.urls import include,path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

router =DefaultRouter()

router.register(r'Userprofile',UserProfilesViewSet)
router.register(r'ticket', TicketViewSet)
router.register(r'salle', SalleViewSet)
router.register(r'film', FilmViewSet)
router.register(r'projection', ProjectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('userprofile/get_user_info/', UserProfilesViewSet.as_view({'post': 'get_user_info'}), name='get_user_info'),
   
]