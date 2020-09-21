from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView ,DetailView
from analytics.signals import object_viewed_signal
from django.http import Http404
from carts.models import Cart
from analytics.mixins import ObjectViewedMixin
# Create your views here.
from .models import Product,ProductManager

class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all().featured()

class ProductFeaturedDetailView(ObjectViewedMixin,DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"
    # -- add a context
    # def get_queryset(self,*args,**kwargs):
    #     request = self.request
    #     return Product.objects.featured()

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context
    # def get_context_data(self,*args,**kwargs):
    #     context = super(ProductListView,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context
    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all()
#the process done in ProductListView:-
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
               'object_list' : queryset
    }
    return render(request,"products/list.html",context)

class ProductDetailSlugView(ObjectViewedMixin,DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        #instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance



class ProductDetailView(ObjectViewedMixin,DetailView):
    # queryset = Product.objects.all()
    template_name = "products/detail.html"
    # -- add a context
    def get_context_data(self,*args,**kwargs):
        context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
        print(context)
        # context['abc'] = 123
        return context

    # def get_object(self,*args,**kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404("Product doesn't exist")
    #     return instance
        def get_queryset(self,*args,**kwargs):
            request = self.request
            pk = self.kwargs.get('pk')
            return Product.objects.filter(pk=pk)

def product_detail_view(request,pk=None,*args,**kwargs):
    #instance = Product.objects.get(pk=pk) #id
    #instance = get_object_or_404(Product, pk=pk)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesn't exist")
    # except:
    #     print("huh?")

    qs  = Product.objects.filter(id=pk)
    #print(qs)
    if qs.exists() and qs.count() == 1: # len(qs)
        instance = qs.first()
    else:
        raise Http404("Product doesn't exist")
    context = {
               'object' : instance
               # 'abc':123
    }
    return render(request,"products/detail.html",context)

class ProductMenListView(ListView):
    template_name = "products/menlist.html"

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all().men()



class ProductWomenListView(ListView):
    template_name = "products/womenlist.html"

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all().women()



class ProductKidsListView(ListView):
    template_name = "products/Kidslist.html"

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all().kids()
