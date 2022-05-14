from django.urls import path
from .views import * 


urlpatterns =   [
    path('', index, name="home"),
    path('turn/<str:id>', turnWashing, name="turnWashing"),
    path('turn/<str:id>', turndryer, name="turndryer"),

    # path('tablel_items/<str:id>', TableItemsViewSet.as_view(),),
]
