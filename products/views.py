from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, CommentForm
from .models import Product, Comment
from django.views.decorators.http import require_POST
from django.contrib import messages

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:index')
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/form.html', context)

def detail(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    form = CommentForm()
    comments = Comment.objects.all()
    context = {
        'product': product,
        'form': form,
        'comments': comments
    }
    return render(request, 'products/detail.html', context)

@require_POST
def comment_create(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    if request.user.is_authenticated:
        if product.comment_set.filter(user=request.user):
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.product_id = product_pk
                comment.save()
                messages.success(request, '상품평이 제출되었습니다!')
        else:
            messages.success(request, '이미 상품평을 제출하셨습니다. 감사합니다!')
        
        return redirect('products:detail', product_pk)
    else:
        return redirect('accounts:login')


