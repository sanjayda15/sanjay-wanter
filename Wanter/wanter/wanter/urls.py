"""wanter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from addresses.views import checkout_address_create_view,checkout_address_reuse_view
# from products.views import (ProductListView,
#                             product_list_view,
#                             product_detail_view,
#                             ProductListView,
#                             ProductDetailView,
#                             ProductFeaturedListView,
#                             ProductFeaturedDetailView,
#                             ProductDetailSlugView)
from django.contrib import admin
from django.urls import path,include
from carts.views import cart_detail_api_view
from . views import (home_page,about_page,practice_page,
                     contact_page,)

urlpatterns = [
    path('',home_page,name='home'),
    path('cart/', include("carts.urls", namespace='cart')),

    path('about/',about_page,name='about'),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
    path('api/cart/', cart_detail_api_view, name='api-cart'),
    path('practice/',practice_page,name='practice'),
     # path('products-fbv/',product_list_view),
    # path('products/',ProductListView.as_view(),name='about_page'),
    # path('featured/',ProductFeaturedListView.as_view(),name='fabout_page'),
    # path('featured/<int:pk>/',ProductFeaturedDetailView.as_view(),name='fabout_page'),
    # path('products-fbv/<int:pk>/',product_detail_view),
    # # path('products/<int:pk>/',ProductDetailView.as_view(),name='about_page'),
    # path('products/<slug>/',ProductDetailSlugView.as_view(),name='about_page'),
    path('billing/',include('billing.urls',namespace='billing')),
    path('products/',include('products.urls',namespace='products')),
    path('search/',include('search.urls',namespace='search')),
    path('contact/',contact_page,name='contact'),
    path('admin/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
