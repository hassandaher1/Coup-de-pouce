import io
import random
from typing import List, Tuple

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from products.models import Product

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover - Pillow is required and already installed
    raise SystemExit("Pillow est requis pour générer des images de démo") from exc


def generate_image(color: Tuple[int, int, int]) -> ContentFile:
    """Génère une petite image PNG en mémoire pour illustrer un produit."""
    img = Image.new("RGB", (800, 600), color=color)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return ContentFile(buffer.read(), name="demo.png")


class Command(BaseCommand):
    help = "Crée des publications de démonstration avec images générées"

    def handle(self, *args, **options):
        demo_items: List[dict] = [
            {
                "title": "Chaise en bois recyclé",
                "description": "Chaise robuste en bois revalorisé, poncée et vernie. Idéale pour une salle à manger ou un coin bureau.",
                "dimensions": "42 x 45 x 90 cm",
                "color": (87, 140, 110),
                "category": "meubles",
            },
            {
                "title": "Table basse palette",
                "description": "Palette upcyclée avec roulettes, plateau vitrifié et coins arrondis pour un style industriel doux.",
                "dimensions": "80 x 60 x 35 cm",
                "color": (231, 143, 90),
                "category": "maison",
            },
            {
                "title": "Lampe de chevet vintage",
                "description": "Pied en métal patiné, abat-jour en tissu beige. Câblage vérifié, fonctionne parfaitement.",
                "dimensions": "Ø 20 x 35 cm",
                "color": (118, 122, 168),
                "category": "maison",
            },
            {
                "title": "Armoire deux portes",
                "description": "Armoire rénovée, peinture mate sable, poignées laiton. Penderie + étagères modulables.",
                "dimensions": "110 x 55 x 190 cm",
                "color": (176, 156, 128),
                "category": "meubles",
            },
            {
                "title": "Vélo de ville reconditionné",
                "description": "Vélo simple vitesse, freins revus, pneus neufs. Idéal trajets urbains.",
                "dimensions": "Taille M, roues 28\"",
                "color": (95, 125, 180),
                "category": "sport",
            },
            {
                "title": "Lot de bocaux en verre",
                "description": "10 bocaux hermétiques nettoyés, parfaits pour vrac ou déco de cuisine.",
                "dimensions": "0,75 L et 1 L",
                "color": (166, 194, 161),
                "category": "culture",
            },
            {
                "title": "Pull en laine upcyclé",
                "description": "Pull chaud confectionné à partir de laine revalorisée, coupe unisexe.",
                "dimensions": "Taille M",
                "color": (180, 126, 126),
                "category": "mode",
            },
            {
                "title": "Jeu de construction en bois",
                "description": "50 pièces en bois issu de chutes, poncées et non traitées. Parfait pour les enfants.",
                "dimensions": "Boîte 25 x 20 x 10 cm",
                "color": (206, 178, 120),
                "category": "jouet",
            },
            {
                "title": "Kit bricolage de base",
                "description": "Marteau, tournevis, pince et mètre ruban remis en état, prêt pour vos petits travaux.",
                "dimensions": "Trousse 30 x 15 x 8 cm",
                "color": (120, 144, 156),
                "category": "bricolage",
            },
        ]

        created = 0
        for item in demo_items:
            obj, exists = Product.objects.get_or_create(
                title=item["title"],
                defaults={
                    "description": item["description"],
                    "dimensions": item["dimensions"],
                    "is_published": True,
                    "category": item["category"],
                },
            )
            if exists:
                color = tuple(item["color"])
                obj.image.save(
                    f"demo_{random.randint(1000,9999)}.png",
                    generate_image(color),
                    save=False,
                )
                obj.image_alt = f"Photo de {obj.title}"
                obj.save()
                created += 1
            else:
                # Si déjà présent, assure la catégorie cohérente sans écraser l'image existante
                if obj.category != item["category"]:
                    obj.category = item["category"]
                    obj.save(update_fields=["category"])

        self.stdout.write(self.style.SUCCESS(f"{created} publications de démonstration créées."))

