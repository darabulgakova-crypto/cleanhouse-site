from django.contrib import admin, messages
from .models import Women, Category, TagPost
from django.utils.safestring import mark_safe

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    ordering = ['-time_create', 'title']
    list_per_page = 5
    search_fields = ['title', 'cat__name']
    list_filter = ['cat__name', 'is_published']
    filter_horizontal = ['tags']
    readonly_fields = ['post_photo']
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
    (None, {
        'fields': ('title', 'slug', 'content', 'photo', 'cat', 'tags', 'post_photo',)
    }),
)
    

    actions = ['set_published', 'set_draft']

    @admin.display(description='Изображение')
    def post_photo(self, women):
        if women.photo: 
            return mark_safe(f"<img src='{women.photo.url}' width=50>")
        return "Без фото"

    @admin.display(description='Краткое описание')
    def brief_info(self, women):
        return f'Описание {len(women.content)} символов'

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, f'Изменено {count} записи(ей)')

    @admin.action(description='Снять публикацию')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(
            request,
            f'{count} записи(ей) сняты с публикации',
            messages.WARNING
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(TagPost)
class TagPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'slug')