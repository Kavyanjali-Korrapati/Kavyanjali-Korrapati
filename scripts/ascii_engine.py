from PIL import Image, ImageOps, ImageFilter

ASCII_RAMP = (
    " .'`^\",:;Il!i~+_-?][}{1)(|\\/"
    "tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
)

def enhance_image(image: Image.Image) -> Image.Image:
    image = ImageOps.autocontrast(image)
    image = image.filter(ImageFilter.SHARPEN)
    image = image.filter(ImageFilter.SHARPEN)
    return image

def resize_image(image: Image.Image, width=80):
    aspect = image.height / image.width

    # Character cells are taller than they are wide.
    height = int(aspect * width * 0.52)

    return image.resize((width, height), Image.Resampling.LANCZOS)

def brightness_to_char(pixel):
    idx = int(pixel / 255 * (len(ASCII_RAMP) - 1))
    return ASCII_RAMP[::-1][idx]

def image_to_ascii(image: Image.Image, width=80):
    image = image.convert("L")
    image = enhance_image(image)
    image = resize_image(image, width)

    pixels = image.load()

    rows = []

    for y in range(image.height):

        line = []

        for x in range(image.width):

            value = pixels[x, y]

            # Make nearly-white pixels disappear
            if value > 245:
                line.append(" ")
            else:
                line.append(brightness_to_char(value))

        rows.append("".join(line).rstrip())

    return rows