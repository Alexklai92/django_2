from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic.list import ListView

from .models import Product, Review
from .forms import ReviewForm

class ProductListView(ListView):
    template_name = 'app/product_list.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = self.model.objects.all()
        return context

# class ProductView(View):
#     template_name = 'app/product_detail.html'
#     form_class = Product
#     pk_url_kwarg = 'pk'
#     query_pk_and_slug = True
#
#     def post(self, request, pk, *args, **kwargs):
#         product = get_object_or_404(Product, id=self.pk_url_kwarg)
#         product_id = request.path.lstrip("/product/").rstrip("/")
#         reviews = Review.objects.all().filter(product=Product.objects.get(id=product_id))
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             review_text = request.POST['text']
#             review = Review.objects.create(text=review_text, product=Product.objects.get(id=product_id))
#         return render(request, self.template_name, {'product': product, 'form': form, 'reviews': reviews})
#
#     def get(self, request, pk, *args, **kwargs):
#         form = self.form_class(request.POST)
#         return render(request, self.template_name, {'form': form})

def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    product_id = pk
    if 'reviewed_products' not in request.session:
        request.session['reviewed_products'] = []
    reviews = Review.objects.all().filter(product=Product.objects.get(id=product_id))
    form = ReviewForm
    if request.method == 'POST':
        request.session['reviewed_products'].append(product_id)
        request.session.save()
        review_text = request.POST['text']
        review = Review(text=review_text, product=Product.objects.get(id=product_id))
        review.save()

    if product_id not in request.session['reviewed_products']:
        context = {
            'form': form,
            'product': product,
            'reviews': reviews
        }
        return render(request, template, context)
    context = {
        'product': product,
        'is_review_exist': True,
        'reviews': reviews
    }
    return render(request, template, context)

# def product_list_view(request):
#     template = 'app/product_list.html'
#     products = Product.objects.all()
#
#     context = {
#         'product_list': products,
#     }
#
#     return render(request, template, context)
