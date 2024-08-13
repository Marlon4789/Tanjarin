from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from blog.models import Article
from form_blocks.forms import SubscriptionForm


# Create your views here.

def show_posts(request):
    quill_posts = Article.objects.all().order_by('-id')
    return render(request, 'content/show_posts.html', {'quill_posts': quill_posts})

def home(request):
    quill_posts = Article.objects.all().order_by('-id')
    return render(request, 'content/home.html', {'quill_posts': quill_posts})


def quillpost_detail(request, quillpost_id):
    quillpost = get_object_or_404(Article, pk=quillpost_id)
    quill_content_html = quillpost.content
    quill_posts = Article.objects.all().order_by('id')

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Correo enviado con éxito.'})
            return render(request, 'content/detail.html', {
                'quill_content_html': quill_content_html,
                'quillpost': quillpost,
                'quill_posts': quill_posts,
                'form': form,
                'success_message': 'Correo enviado con éxito.'
            })
    else:
        form = SubscriptionForm()

    return render(request, 'content/detail.html', {
        'quill_content_html': quill_content_html,
        'quillpost': quillpost,
        'quill_posts': quill_posts,
        'form': form,
        'success_message': ''  # Inicializar mensaje vacío
    })