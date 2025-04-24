from dataclasses import dataclass
import math
@dataclass
class Star:
    index: int
    x: float
    y: float
    z: float
    xr: float
    yr: float
    zr: float
    thetar: float
    phir: float
    posX: int
    posY: int
    visivel: bool
    rgb_estrela: str
    rgb_designacao: str
    rgb_var: str
    designacao: str
    magnitude: float
    tamanho: int

    def __init__(self, index, x, y, z, rgb_estrela, rgb_designacao, designacao, magnitude):
        self.index = int(index)
        self.x, self.y, self.z = float(x), float(y), float(z)

        self.rgb_estrela = rgb_estrela
        self.rgb_designacao = rgb_designacao
        self.rgb_var = "FFFFFF"

        if designacao == "": self.designacao == ""
        else: self.designacao == designacao[3:]

        self.magnitude = magnitude
        self.tamanho = Star.size(magnitude)

        self.rotate()
        self.position()
        return None
    
    def rotate(self, R: list = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]):
        xr = self.x * R[0][0] + self.y * R[0][1] + self.z * R[0][2]
        yr = self.x * R[1][0] + self.y * R[1][1] + self.z * R[1][2]
        zr = self.x * R[2][0] + self.y * R[2][1] + self.z * R[2][2]
        self.xr, self.yr, self.zr = xr, yr, zr
        self.thetar, self.phir = Star.toAngles(xr, yr, zr)
        return None
    
    def position(self):
        posX = round(((self.thetar + math.pi / 4) % (2 * math.pi)) * 1000)
        posY = round((((self.phir + 3 * math.pi / 4) % math.pi) - math.pi / 2) * 1000)
        if not 0 <= posX < 1572:
            self.posX, self.posY, self.visivel = -1, -1, False
        if not 0 <= posY < 1572:
            self.posX, self.posY, self.visivel = -1, -1, False
        self.posX, self.posY, self.visivel = posX, posY, True
        return None
    
    def color(self, rgb: str):
        self.rgb_var = rgb
        return None
    
    @staticmethod
    def line(origin, destination):
        if origin.visivel and destination.visivel:
            return origin.posX, origin.posY, destination.posX, destination.posY
        return None
    
    @staticmethod
    def size(magnitude: float):
        if   magnitude < 0.8: return 10
        elif magnitude < 0.0: return 8
        elif magnitude < 1.2: return 6
        elif magnitude < 2.0: return 5
        elif magnitude < 3.0: return 4
        elif magnitude < 5.0: return 3
        elif magnitude < 6.0: return 2
        return 1
    
    @staticmethod
    def toAngles(x: float, y: float, z: float):
        theta = math.atan(y / x) + (x > 0 and y < 0) * 2 * math.pi + (x <= 0) * math.pi
        phi = math.asin(z)
        return theta, phi
    
    @staticmethod
    def toCoords(theta: float, phi: float):
        x = math.cos(theta) * math.cos(phi)
        y = math.sin(theta) * math.cos(phi)
        z = math.sin(phi)
        return x, y, z
    