from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Contact, Experience, Project, ProjectImage, Skill


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "order"]
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ["order"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "is_featured", "order", "created_at", "image_preview"]
    list_filter = ["category", "is_featured", "created_at"]
    list_editable = ["is_featured", "order"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "description"]
    inlines = [ProjectImageInline]

    def image_preview(self, obj):
        if obj.main_image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 5px;" />',
                obj.main_image.url,
            )
        return "Нет изображения"

    image_preview.short_description = "Превью"


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "level", "order"]
    list_filter = ["category"]
    list_editable = ["level", "order"]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["position", "company", "start_date", "end_date", "is_current"]
    list_filter = ["is_current", "start_date"]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "created_at", "is_read"]
    list_filter = ["is_read", "created_at"]
    list_editable = ["is_read"]
    readonly_fields = ["name", "email", "subject", "message", "created_at"]
