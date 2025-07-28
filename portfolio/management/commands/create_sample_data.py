from django.core.management.base import BaseCommand

from portfolio.models import Category, Experience, Project, Skill


class Command(BaseCommand):
    help = "Добавляет тестовые данные для портфолио"

    def handle(self, *args, **options):
        self.stdout.write("Создание тестовых данных...")

        # Создание категорий
        web_category, created = Category.objects.get_or_create(
            name="Веб-разработка", defaults={"slug": "web-development", "order": 1}
        )

        bot_category, created = Category.objects.get_or_create(
            name="Telegram боты", defaults={"slug": "telegram-bots", "order": 2}
        )

        api_category, created = Category.objects.get_or_create(
            name="API разработка", defaults={"slug": "api-development", "order": 3}
        )

        # Создание навыков
        skills_data = [
            ("Python", "fab fa-python", 90, "Языки программирования"),
            ("JavaScript", "fab fa-js-square", 85, "Языки программирования"),
            ("HTML/CSS", "fab fa-html5", 95, "Frontend"),
            ("Django", "fab fa-python", 88, "Backend фреймворки"),
            ("FastAPI", "fas fa-rocket", 82, "Backend фреймворки"),
            ("React", "fab fa-react", 75, "Frontend"),
            ("PostgreSQL", "fas fa-database", 80, "Базы данных"),
            ("Docker", "fab fa-docker", 70, "DevOps"),
            ("Git", "fab fa-git-alt", 90, "Инструменты"),
            ("Aiogram", "fas fa-robot", 85, "Боты"),
        ]

        for name, icon, level, category in skills_data:
            Skill.objects.get_or_create(
                name=name, defaults={"icon": icon, "level": level, "category": category, "order": 0}
            )

        # Создание опыта работы
        Experience.objects.get_or_create(
            company="Freelance",
            position="Full-stack разработчик",
            defaults={
                "description": "Разработка веб-приложений и Telegram ботов для различных клиентов. Создание RESTful API, интеграция с внешними сервисами, оптимизация производительности.",
                "start_date": "2023-01-01",
                "is_current": True,
            },
        )

        Experience.objects.get_or_create(
            company="IT Startup",
            position="Python разработчик",
            defaults={
                "description": "Участие в разработке MVP продукта, создание микросервисной архитектуры, работа с командой из 5 человек.",
                "start_date": "2022-06-01",
                "end_date": "2022-12-31",
                "is_current": False,
            },
        )

        # Создание проектов
        projects_data = [
            {
                "title": "Интернет-магазин на Django",
                "slug": "django-ecommerce",
                "short_description": "Полнофункциональный интернет-магазин с корзиной, оплатой и админ-панелью",
                "description": """Этот проект представляет собой современный интернет-магазин, разработанный с использованием Django и современных веб-технологий.

Основные возможности:
• Каталог товаров с фильтрацией и поиском
• Корзина покупок с возможностью изменения количества
• Система регистрации и авторизации пользователей
• Интеграция с платежными системами
• Административная панель для управления товарами
• Адаптивный дизайн для всех устройств

Использованные технологии позволили создать быстрое и надежное решение для электронной коммерции.""",
                "category": web_category,
                "technologies": "Django, PostgreSQL, HTML/CSS, JavaScript, Bootstrap, Stripe API",
                "demo_url": "https://example-shop.com",
                "github_url": "https://github.com/yourusername/django-shop",
                "is_featured": True,
                "order": 1,
            },
            {
                "title": "Telegram бот помощник",
                "slug": "telegram-assistant-bot",
                "short_description": "Умный бот для автоматизации задач и уведомлений",
                "description": """Многофункциональный Telegram бот, созданный для автоматизации повседневных задач.

Возможности бота:
• Напоминания и планировщик задач
• Интеграция с внешними API для получения информации
• Система уведомлений
• Многоязычная поддержка
• Админ-панель для управления

Бот обрабатывает более 1000 запросов в день и имеет высокие оценки пользователей.""",
                "category": bot_category,
                "technologies": "Python, Aiogram, PostgreSQL, Redis, Docker",
                "github_url": "https://github.com/yourusername/telegram-bot",
                "is_featured": True,
                "order": 2,
            },
            {
                "title": "REST API для мобильного приложения",
                "slug": "mobile-app-api",
                "short_description": "Высокопроизводительное API с документацией и тестами",
                "description": """REST API, разработанное для мобильного приложения с использованием FastAPI.

Особенности API:
• Автоматическая документация с Swagger
• JWT аутентификация
• Валидация данных с Pydantic
• Кэширование с Redis
• Comprehensive тестирование
• Docker контейнеризация

API обслуживает более 10,000 активных пользователей ежедневно.""",
                "category": api_category,
                "technologies": "Python, FastAPI, PostgreSQL, Redis, Docker, Pytest",
                "demo_url": "https://api-docs.example.com",
                "github_url": "https://github.com/yourusername/mobile-api",
                "is_featured": True,
                "order": 3,
            },
        ]

        for project_data in projects_data:
            Project.objects.get_or_create(slug=project_data["slug"], defaults=project_data)

        self.stdout.write(self.style.SUCCESS("Тестовые данные успешно созданы!"))
