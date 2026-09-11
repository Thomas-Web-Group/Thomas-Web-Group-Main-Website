from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent
IMAGE_DIR = ROOT / "assets" / "img"

MAX_WIDTH = 1600
WEBP_QUALITY = 82

extensions = {".jpg", ".jpeg", ".png"}

for image_path in IMAGE_DIR.rglob("*"):
    if not image_path.is_file():
        continue

    if image_path.suffix.lower() not in extensions:
        continue

    output_path = image_path.with_suffix(".webp")

    if output_path.exists():
        print(f"SKIPPED: {output_path.name}")
        continue

    try:
        with Image.open(image_path) as original:
            img = ImageOps.exif_transpose(original)

            if img.width > MAX_WIDTH:
                new_height = round(img.height * MAX_WIDTH / img.width)
                img = img.resize(
                    (MAX_WIDTH, new_height),
                    Image.Resampling.LANCZOS
                )

            if img.mode not in ("RGB", "RGBA"):
                img = img.convert(
                    "RGBA" if "transparency" in img.info else "RGB"
                )

            img.save(
                output_path,
                "WEBP",
                quality=WEBP_QUALITY,
                method=6
            )

            old_kb = image_path.stat().st_size / 1024
            new_kb = output_path.stat().st_size / 1024

            print(
                f"{image_path.name}: "
                f"{old_kb:.0f} KB -> {new_kb:.0f} KB"
            )

    except Exception as e:
        print(f"ERROR: {image_path}: {e}")