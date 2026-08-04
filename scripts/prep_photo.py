import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image
from rembg import remove


def preprocess(image_path):
    image_path = Path(image_path)

    if not image_path.exists():
        print(f"Image not found: {image_path}")
        return

    print("Loading image...")
    image = Image.open(image_path).convert("RGBA")

    print("Removing background...")
    image = remove(image)

    image_np = np.array(image)

    alpha = image_np[:, :, 3] / 255.0

    white = np.ones_like(image_np[:, :, :3]) * 255

    rgb = image_np[:, :, :3]

    composite = (
        rgb * alpha[:, :, None]
        + white * (1 - alpha[:, :, None])
    ).astype(np.uint8)

    gray = cv2.cvtColor(composite, cv2.COLOR_RGB2GRAY)

    print("Applying CLAHE...")
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(gray)

    output = image_path.parent / "source-prepped.png"

    cv2.imwrite(str(output), enhanced)

    print(f"Saved to {output}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage:")
        print("python scripts/prep_photo.py assets/source-photo.jpg")
        sys.exit()

    preprocess(sys.argv[1])