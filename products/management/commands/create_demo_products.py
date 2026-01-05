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
            # Maison - produits supplémentaires
            {
                "title": "Vase en céramique artisanale",
                "description": "Vase unique fait main à partir de céramique recyclée. Parfait pour fleurs séchées ou déco.",
                "dimensions": "Ø 15 x 25 cm",
                "color": (200, 180, 150),
                "category": "maison",
            },
            {
                "title": "Set de coussins récup",
                "description": "3 coussins confectionnés à partir de tissus récupérés, housses lavables, rembourrage naturel.",
                "dimensions": "40 x 40 cm chacun",
                "color": (150, 130, 180),
                "category": "maison",
            },
            # Mode - produits supplémentaires
            {
                "title": "Sac à main en cuir upcyclé",
                "description": "Sac en cuir véritable récupéré et retravaillé, doublure intérieure, fermeture éclair fonctionnelle.",
                "dimensions": "35 x 28 x 12 cm",
                "color": (100, 80, 60),
                "category": "mode",
            },
            {
                "title": "Écharpe tricotée main",
                "description": "Écharpe en laine recyclée, tricotée à la main, motifs géométriques, très douce.",
                "dimensions": "180 x 30 cm",
                "color": (140, 100, 120),
                "category": "mode",
            },
            # Jouet - produits supplémentaires
            {
                "title": "Poupée en tissu faite main",
                "description": "Poupée douce confectionnée à partir de chutes de tissu, rembourrage naturel, lavable.",
                "dimensions": "30 cm de haut",
                "color": (220, 180, 160),
                "category": "jouet",
            },
            {
                "title": "Puzzle en bois recyclé",
                "description": "Puzzle 50 pièces en bois issu de chutes, motifs animaux, adapté dès 4 ans.",
                "dimensions": "30 x 20 cm",
                "color": (180, 160, 140),
                "category": "jouet",
            },
            # Bricolage - produits supplémentaires
            {
                "title": "Étagère murale palette",
                "description": "Étagère fabriquée à partir de palette recyclée, poncée et traitée, 3 niveaux.",
                "dimensions": "80 x 25 x 60 cm",
                "color": (160, 140, 110),
                "category": "bricolage",
            },
            {
                "title": "Boîte à outils vintage",
                "description": "Boîte métallique rénovée contenant outils de base : clés, vis, boulons, etc.",
                "dimensions": "40 x 25 x 15 cm",
                "color": (100, 100, 100),
                "category": "bricolage",
            },
            # Culture - produits supplémentaires
            {
                "title": "Livres d'occasion sélectionnés",
                "description": "Lot de 5 livres en bon état, genres variés : roman, BD, guide pratique.",
                "dimensions": "Format standard",
                "color": (180, 150, 130),
                "category": "culture",
            },
            {
                "title": "Cadre photo en bois recyclé",
                "description": "Cadre photo fait main à partir de bois récupéré, plusieurs tailles disponibles.",
                "dimensions": "20 x 25 cm",
                "color": (140, 120, 100),
                "category": "culture",
            },
            # Sport - produits supplémentaires
            {
                "title": "Raquettes de badminton",
                "description": "Paire de raquettes reconditionnées, cordage vérifié, manches en bon état.",
                "dimensions": "Longueur 68 cm",
                "color": (200, 200, 200),
                "category": "sport",
            },
            {
                "title": "Haltères ajustables",
                "description": "Paire d'haltères avec poids ajustables, barre centrale en bon état.",
                "dimensions": "Poids max 10 kg par haltère",
                "color": (80, 80, 80),
                "category": "sport",
            },
            # Meubles - produits supplémentaires
            {
                "title": "Étagère bibliothèque",
                "description": "Étagère 5 niveaux en bois massif rénovée, idéale pour livres ou déco.",
                "dimensions": "80 x 30 x 150 cm",
                "color": (120, 100, 80),
                "category": "meubles",
            },
            {
                "title": "Tabouret bar upcyclé",
                "description": "Tabouret haut rénové, assise en cuir récupéré, pieds métal peint.",
                "dimensions": "Ø 35 x 75 cm",
                "color": (90, 70, 50),
                "category": "meubles",
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

