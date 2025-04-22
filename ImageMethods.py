from PIL import Image, ImageDraw
class ImageMethods:
    @staticmethod
    def create():
        return Image.new("RGB", (1572, 1572), (0, 0, 0))
    
    @staticmethod
    def paintPixel(image, x, y, r, g, b):
        image.putpixel((x,y), (r, g, b))
        return None
    
    @staticmethod
    def paintCircle(image, x, y, size, r, g, b):
        assert 0 <= x < 1572
        assert 0 <= y < 1572
        assert 0 < size <= 10
        malha = [[15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
                 [15, 15, 15, 15, 15, 15, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15],
                 [15, 15, 15, 15, 10, 10,  9,  9,  9,  9,  9,  9,  9,  9,  9, 10, 10, 15, 15, 15, 15],
                 [15, 15, 15, 10, 10,  9,  9,  8,  8,  8,  8,  8,  8,  8,  9,  9, 10, 10, 15, 15, 15],
                 [15, 15, 10, 10,  9,  8,  8,  7,  7,  7,  7,  7,  7,  7,  8,  8,  9, 10, 10, 15, 15],
                 [15, 15, 10,  9,  8,  8,  7,  6,  6,  6,  6,  6,  6,  6,  7,  8,  8,  9, 10, 15, 15],
                 [15, 10,  9,  9,  8,  7,  6,  6,  5,  5,  5,  5,  5,  6,  6,  7,  8,  9,  9, 10, 15],
                 [15, 10,  9,  8,  7,  6,  6,  5,  4,  4,  4,  4,  4,  5,  6,  6,  7,  8,  9, 10, 15],
                 [15, 10,  9,  8,  7,  6,  5,  4,  3,  3,  3,  3,  3,  4,  5,  6,  7,  8,  9, 10, 15],
                 [15, 10,  9,  8,  7,  6,  5,  4,  3,  2,  2,  2,  3,  4,  5,  6,  7,  8,  9, 10, 15],
                 [15, 10,  9,  8,  7,  6,  5,  4,  3,  2,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 15],
                 [15, 10,  9,  8,  7,  6,  5,  4,  3,  2,  2,  2,  3,  4,  5,  6,  7,  8,  9, 10, 15],
                 [15, 10,  9,  8,  7,  6,  5,  4,  3,  3,  3,  3,  3,  4,  5,  6,  7,  8,  9, 10, 15],
                 [15, 10,  9,  8,  7,  6,  6,  5,  4,  4,  4,  4,  4,  5,  6,  6,  7,  8,  9, 10, 15],
                 [15, 10,  9,  9,  8,  7,  6,  6,  5,  5,  5,  5,  5,  6,  6,  7,  8,  9,  9, 10, 15],
                 [15, 15, 10,  9,  8,  8,  7,  6,  6,  6,  6,  6,  6,  6,  7,  8,  8,  9, 10, 15, 15],
                 [15, 15, 10, 10,  9,  8,  8,  7,  7,  7,  7,  7,  7,  7,  8,  8,  9, 10, 10, 15, 15],
                 [15, 15, 15, 10, 10,  9,  9,  8,  8,  8,  8,  8,  8,  8,  9,  9, 10, 10, 15, 15, 15],
                 [15, 15, 15, 15, 10, 10,  9,  9,  9,  9,  9,  9,  9,  9,  9, 10, 10, 15, 15, 15, 15],
                 [15, 15, 15, 15, 15, 15, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15],
                 [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]]
        for dx, i in enumerate(range(x - 10, x + 11)):
            if not 0 <= i < 1572: continue
            for dy, j in enumerate(range(y - 10, y + 11)):
                if not 0 <= j < 1572: continue
                if malha[dy][dx] > size: continue
                ImageMethods.paintPixel(image, i, j, r, g, b)
        return None
    
    @staticmethod
    def paintLine(image, x, y, xf, yf, r, g, b):
        assert 0 <= x <= xf < 1572
        assert 0 <= y <= yf < 1572
        if (xf - x) >= (yf - y):
            for dx, i in enumerate(range(x, xf)):
                if dx == 0: continue
                dy = round(dx * (yf - y) / (xf - x))
                ImageMethods.paintPixel(image, i, y + dy, r, g, b)
        else:
            for dy, j in enumerate(range(y, yf)):
                if dy == 0: continue
                dx = round(dy * (xf - x) / (yf - y))
                ImageMethods.paintPixel(image, x + dx, j, r, g, b)
        return None

    @staticmethod
    def drawCircle(image, x, y, size, r, g, b):
        assert 0 <= x < 1572
        assert 0 <= y < 1572
        assert 0 < size <= 10
        draw = ImageDraw.Draw(image)
        draw.ellipse((x - size, y - size, x + size, y + size), fill=(r, g, b))
        return None
    
    @staticmethod
    def drawLine(image, x, y, xf, yf, r, g, b):
        assert 0 <= x <= xf < 1572
        assert 0 <= y <= yf < 1572
        draw = ImageDraw.Draw(image)
        draw.line((x, y, xf, yf), fill=(r, g, b), width=1)
        return None
