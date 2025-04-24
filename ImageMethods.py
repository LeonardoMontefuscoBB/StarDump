from PIL import Image, ImageDraw
from dataclasses import dataclass

@dataclass
class ImageMethods:
    @staticmethod
    def create():
        return Image.new("RGB", (1572, 1572), (255, 255, 255)) #flag para impressao
        # return Image.new("RGB", (1572, 1572), (0, 0, 0))
    
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
        # if size == 1: size = 0.5
        # if size == 2: size = 1.0
        # if size == 3: size = 1.5
        # if size == 4: size = 2.0
        # if size == 5
        draw = ImageDraw.Draw(image)
        if r == 105: r, g, b =  31,  73, 125 #flag para impressao
        if r == 188: r, g, b = 148, 138,  84 #flag para impressao
        if r == 93:  r, g, b =  49, 134, 155 #flag para impressao
        if r == 247: r, g, b = 226, 107,  10 #flag para impressao
        if r == 178: r, g, b =  89,  89,  89 #flag para impressao
        if size < 3:
            draw.ellipse((y - size / 2, 1571 - x - size / 2, y + size / 2, 1571 - x + size / 2), fill=(r, g, b))
        elif size < 4:
            draw.ellipse((y - size / 1.5, 1571 - x - size / 1.5, y + size / 1.5, 1571 - x + size / 1.5), fill=(r, g, b))
        else:
            draw.ellipse((y - size, 1571 - x - size, y + size, 1571 - x + size), fill=(r, g, b))
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