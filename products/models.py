from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("maison", "Maison"),
        ("mode", "Mode"),
        ("jouet", "Jouet"),
        ("bricolage", "Bricolage"),
        ("culture", "Culture"),
        ("sport", "Sport"),
        ("meubles", "Meubles"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    dimensions = models.CharField(max_length=255, blank=True, help_text="Ex: 120 x 80 x 60 cm")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="maison")
    image = models.ImageField(upload_to="products/")
    image_alt = models.CharField("Texte alternatif de la photo", max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title
