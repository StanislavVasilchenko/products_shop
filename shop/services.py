from io import BytesIO
from django.core.files.base import ContentFile
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


def converting_image(base_image: InMemoryUploadedFile) -> tuple[ContentFile, ContentFile]:
    """Преобразование базового изображения в разные размеры.
    Принимает на вход базовое загруженное изображение, преобразовавыает его
    к размерам в 2 и в 3 раза меньше.
    Возвращает кортеж из изображений типа ContentFile"""

    image = Image.open(base_image)
    middle = image.resize((image.width // 2, image.height // 2))
    small = image.resize((image.width // 3, image.height // 3))
    image_io = BytesIO()
    middle.save(image_io, format='PNG')
    image_io.seek(0)
    small.save(image_io, format='PNG')
    image_io.seek(0)
    image_middle = ContentFile(image_io.read(), name=f'middle_{base_image.name}')
    image_small = ContentFile(image_io.read(), name=f'small_{base_image.name}')
    return image_middle, image_small
