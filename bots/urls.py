from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bots.views import BotViewSet, ScenarioViewSet, StepViewSet

router = DefaultRouter()
router.register('bots', BotViewSet)
router.register('scenarios', ScenarioViewSet)
router.register('steps', StepViewSet)

urlpatterns = [


]

urlpatterns.extend(router.urls)