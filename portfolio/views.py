from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Category, Skill, Experience, Contact
import json


def home(request):
    """Главная страница портфолио"""
    featured_projects = Project.objects.filter(is_featured=True)[:6]
    categories = Category.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()[:3]  # Показываем только последние 3
    
    context = {
        'featured_projects': featured_projects,
        'categories': categories,
        'skills': skills,
        'experiences': experiences,
    }
    return render(request, 'portfolio/home.html', context)


def projects(request):
    """Страница всех проектов"""
    category_slug = request.GET.get('category')
    projects_list = Project.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        projects_list = projects_list.filter(category=category)
    else:
        category = None
    
    categories = Category.objects.all()
    
    context = {
        'projects': projects_list,
        'categories': categories,
        'current_category': category,
    }
    return render(request, 'portfolio/projects.html', context)


def project_detail(request, slug):
    """Детальная страница проекта"""
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.filter(category=project.category).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'portfolio/project_detail.html', context)


def about(request):
    """Страница обо мне"""
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    
    context = {
        'skills': skills,
        'experiences': experiences,
    }
    return render(request, 'portfolio/about.html', context)


def contact(request):
    """Страница контактов"""
    return render(request, 'portfolio/contact.html')


@csrf_exempt
@require_POST
def send_message(request):
    """AJAX обработка отправки сообщения"""
    try:
        data = json.loads(request.body)
        
        # Создаем объект сообщения
        contact = Contact.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            subject=data.get('subject'),
            message=data.get('message')
        )
        
        # Отправляем email (опционально)
        # send_mail(
        #     f"Новое сообщение: {contact.subject}",
        #     f"От: {contact.name} ({contact.email})\n\n{contact.message}",
        #     settings.DEFAULT_FROM_EMAIL,
        #     ['your-email@example.com'],
        #     fail_silently=False,
        # )
        
        return JsonResponse({
            'success': True,
            'message': 'Сообщение успешно отправлено!'
        })
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'Произошла ошибка при отправке сообщения.'
        })


def get_projects_ajax(request):
    """AJAX получение проектов для фильтрации"""
    category_slug = request.GET.get('category')
    
    projects_list = Project.objects.all()
    if category_slug and category_slug != 'all':
        projects_list = projects_list.filter(category__slug=category_slug)
    
    projects_data = []
    for project in projects_list:
        projects_data.append({
            'id': project.id,
            'title': project.title,
            'slug': project.slug,
            'short_description': project.short_description,
            'main_image': project.main_image.url if project.main_image else '',
            'technologies': project.get_technologies_list(),
            'demo_url': project.demo_url,
            'github_url': project.github_url,
        })
    
    return JsonResponse({'projects': projects_data})
