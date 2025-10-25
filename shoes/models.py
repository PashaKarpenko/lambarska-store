from django.db import models
from django.utils import timezone


class SeasonChoices(models.TextChoices):
    spring_summer = 'весна-літо', 'весна-літо'
    autumn_winter = 'осінь-зима', 'осінь-зима'


class Type(models.Model): 
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Тип взуття"
        verbose_name_plural = "Типи взуття"


class Material(models.Model):
    material = models.CharField(max_length=50)

    def __str__(self):
        return self.material

    class Meta:
        verbose_name = "Матеріал"
        verbose_name_plural = "Матеріали"


class Color(models.Model):
    color = models.CharField(max_length=50)


    def __str__(self):
        return self.color

    class Meta:
        verbose_name = "Колір"
        verbose_name_plural = "Кольори"


class Shoe(models.Model):
    name = models.CharField("назва взуття", max_length=255, unique=True)
    price = models.DecimalField("ціна", max_digits=8, decimal_places=0)
    image = models.ImageField("головне фото товару", upload_to='images/main_image')
    type = models.ForeignKey(Type, verbose_name="тип взуття", null=True, on_delete=models.SET_NULL)
    size_from = models.IntegerField("розмір з",max_length=10, null=True, default=36)
    size_to = models.IntegerField("розмір по", max_length=10, null=True, default=41)
    color = models.ForeignKey(Color, verbose_name="колір", null=True, on_delete=models.SET_NULL)
    season = models.CharField("сезон", max_length=10, choices=SeasonChoices.choices)
    material = models.ForeignKey(Material, verbose_name="матеріал", null=True, on_delete=models.SET_NULL)
    is_bestseller = models.BooleanField("бестселер", default=False)
    is_new_shoes = models.BooleanField("нові надходження", default=False)
    is_active = models.BooleanField("товар на сайті", default=True)
    created_at = models.DateTimeField("дата створення товару",auto_now_add=True)
    updated_at = models.DateTimeField("дата оновлення товару", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Список взуття"
        verbose_name_plural = "Список взуття"


class ShoeImage(models.Model):
    shoe = models.ForeignKey(Shoe, related_name='images', on_delete=models.CASCADE, verbose_name="Товар")
    image = models.ImageField(upload_to='images/shoes/', verbose_name="Фото товару")

    def __str__(self):
        return f"{self.shoe.name} - Image {self.id}"

    class Meta:
        verbose_name = "Фото товару"
        verbose_name_plural = "Фото товару"