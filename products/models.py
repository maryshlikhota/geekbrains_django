from django.db import models

# ОРМ
class Category(models.Model):
    title = models.CharField(
        max_length=250
    )
    snippet = models.TextField(
        # пустые строки
        blank=True,
        # отсутсвующее значение
        null=True
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(
        max_length=250
    )
    category = models.ForeignKey(
        Category,
        # поведение триггера если мы удалим категорию
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    image = models.ForeignKey(
        'images.Image',
        on_delete=models.PROTECT
    )
    # image = models.ImageField(
    #     # имя директории, куда загружаются картинки
    #     upload_to='products'
    # )
    # десятичные значения
    cost = models.DecimalField(
        # максимальное кол-во цифр
        max_digits=12,
        # кол-во символов после запятой
        decimal_places=2,
        # по умолчанию
        default=0
    )
    snippet = models.TextField(
        # пустые строки
        blank=True,
        # отсутсвующее значение
        null=True 
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        # один раз автоматиески выставит время при создании
        auto_now_add=True
    )

    def __str__(self):
        return self.title
