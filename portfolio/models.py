from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="URL")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["order"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="URL")
    description = models.TextField(verbose_name="Описание")
    short_description = models.CharField(max_length=300, verbose_name="Краткое описание")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    # Изображения
    main_image = models.ImageField(upload_to="projects/main/", verbose_name="Главное изображение")
    preview_image = models.ImageField(
        upload_to="projects/preview/", verbose_name="Превью изображение", null=True, blank=True
    )

    # Ссылки
    demo_url = models.URLField(verbose_name="Ссылка на демо", null=True, blank=True)
    github_url = models.URLField(verbose_name="Ссылка на GitHub", null=True, blank=True)

    # Технологии
    technologies = models.CharField(max_length=500, verbose_name="Технологии (через запятую)")

    # Метаданные
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_featured = models.BooleanField(default=False, verbose_name="Рекомендуемый")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ["-is_featured", "order", "-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolio:project_detail", kwargs={"slug": self.slug})

    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(",") if tech.strip()]


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images", verbose_name="Проект"
    )
    image = models.ImageField(upload_to="projects/gallery/", verbose_name="Изображение")
    title = models.CharField(max_length=200, verbose_name="Заголовок", null=True, blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Изображение проекта"
        verbose_name_plural = "Изображения проектов"
        ordering = ["order"]

    def __str__(self):
        return f"{self.project.title} - {self.title or 'Изображение'}"


class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    icon = models.CharField(
        max_length=100, verbose_name="Иконка (CSS класс)", null=True, blank=True
    )
    level = models.PositiveIntegerField(default=50, verbose_name="Уровень (1-100)")
    category = models.CharField(max_length=100, verbose_name="Категория")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
        ordering = ["category", "order"]

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField(max_length=200, verbose_name="Компания")
    position = models.CharField(max_length=200, verbose_name="Должность")
    description = models.TextField(verbose_name="Описание")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания", null=True, blank=True)
    is_current = models.BooleanField(default=False, verbose_name="Текущая работа")
    company_url = models.URLField(verbose_name="Сайт компании", null=True, blank=True)

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.position} в {self.company}"


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Тема")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"
