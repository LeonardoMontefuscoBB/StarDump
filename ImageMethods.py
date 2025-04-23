from PIL import Image, ImageDraw
from dataclasses import dataclass

@dataclass
class ImageMethods:
    @staticmethod
    def create():
        return Image.new("RGB", (1572, 1572), (0, 0, 0))
    
    @staticmethod
    def paintPixel(image: Image.Image, x: int, y: int, r: int, g: int, b: int):
        assert 0 <= x < 1572
        assert 0 <= y < 1572
        assert 0 <= r < 256
        assert 0 <= g < 256
        assert 0 <= b < 256
        image.putpixel((x, y), (r, g, b))
        return None

    @staticmethod
    def drawCircle(image: Image.Image, x: int, y: int, size: int, r: int, g: int, b: int):
        assert 0 <= x < 1572
        assert 0 <= y < 1572
        assert 0 < size
        assert 0 <= r < 256
        assert 0 <= g < 256
        assert 0 <= b < 256
        draw = ImageDraw.Draw(image)
        draw.ellipse((x - size, y - size, x + size, y + size), fill=(r, g, b))
        return None
    
    @staticmethod
    def drawLine(image: Image.Image, x: int, y: int, xf: int, yf: int, r: int, g: int, b: int, width: int = 1):
        assert 0 <= x  < 1572
        assert 0 <= xf < 1572
        assert 0 <= y  < 1572
        assert 0 <= yf < 1572
        assert 0 <= r < 256
        assert 0 <= g < 256
        assert 0 <= b < 256
        draw = ImageDraw.Draw(image)
        draw.line((x, y, xf, yf), fill=(r, g, b), width=width)
        return None

if __name__ == "__main__":
    img = ImageMethods.create()
    for i in range(1572):
        ImageMethods.paintPixel(img, i, i, 105, 216, 255)
    ImageMethods.drawLine(img, 25, 1000, 275, 1500, 255, 255, 102)
    ImageMethods.drawCircle(img, 850, 250, 10, 158, 94, 206)

    ImageMethods.drawLine(img, 900, 900, 800, 800, 247, 157, 83)
    ImageMethods.drawLine(img, 900, 900, 800, 900, 247, 157, 83)
    ImageMethods.drawLine(img, 900, 900, 800, 1000, 247, 157, 83)
    ImageMethods.drawLine(img, 900, 900, 900, 800, 247, 157, 83)
    ImageMethods.drawLine(img, 900, 900, 900, 1000, 247, 157, 83)
    ImageMethods.drawLine(img, 900, 900, 1000, 800, 247, 157, 83)
    ImageMethods.drawLine(img, 900, 900, 1000, 900, 247, 157, 83)
    ImageMethods.drawLine(img, 900, 900, 1000, 1000, 247, 157, 83, 10)

    ImageMethods.drawCircle(img, 1400, 900, 200, 156, 187, 89)
    img.save("/home/wsl/LLL/dev/github/StarDump/test.jpg")