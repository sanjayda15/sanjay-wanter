from django.urls import path
from .views import (
        ProductListView,
        ProductDetailSlugView,
        ProductMenListView,
        ProductWomenListView,
        ProductKidsListView,        )

app_name = 'products'
urlpatterns = [
    path('menlist/',ProductMenListView.as_view(),name='menlist'),

    path('womenlist/',ProductWomenListView.as_view(),name='womenlist'),

    path('kidslist/',ProductKidsListView.as_view(),name='kidslist'),

    path('',ProductListView.as_view(),name='list'),
    path('<slug>/',ProductDetailSlugView.as_view(),name='detail'),
    ]
