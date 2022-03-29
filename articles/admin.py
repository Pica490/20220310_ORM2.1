from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Topics, Section

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:

            if form.cleaned_data.get('main_section') == True:
                i=i+1

            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
        if i > 1:
            raise ValidationError('Укажите только один основной раздел')
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        return super().clean()  # вызываем базовый код переопределяемого метода

class RelationshipInline(admin.TabularInline):
    model = Topics
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_filter = ['sname']

@admin.register(Topics)
class TopicsAdmin(admin.ModelAdmin):
    list_filter = ['main_section']

