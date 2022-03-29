from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['title']


    def __str__(self):
        return self.title

class Section(models.Model):

    sname = models.CharField(max_length=30, verbose_name = 'Раздел')

    sections = models.ManyToManyField(
        Article,
        through='Topics',
        through_fields=('article', 'section')
    )

    class Meta:
        ordering = ['sname']


    def __str__(self):
        return self.sname

class Topics(models.Model):

    article = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='scopes',verbose_name = 'Раздел')
    section = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    main_section = models.BooleanField(null=True, blank=True, verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематика статей'

        ordering = ['article']




