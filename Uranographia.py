from dataclasses import dataclass
from io import TextIOBase
import os

from Table import Table
from Star import Star
from Constellation import Constellation
from ImageMethods import ImageMethods
from ColorMethods import ColorMethods

@dataclass
class Uranographia:
    sections: dict
    def __init__(self):
        self.sections = {}
        return None
    
    def subdivide(self, c: Constellation):
        self.sections[c.index] = c
        return None
    
    def populate(self, c_index: int, s: Star, specialDesignation: str = ""):
        self.sections[c_index].populate(s, specialDesignation)
        return None
    
    def rotate(self, c_index: int = 0):
        if c_index == 0:
            R = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        else:
            R = self.sections[c_index].R
        
        for c in self.sections.values():
            for s in c.set.values():
                s.rotate(R)
        return None
    
    def show(self, option: int = 0, reference: int = -1, file="out.png"):
        if reference >= 0: self.rotate(reference)
        match option:
            case 0: self.showRealistic(file)
            case 1: self.showDesignation(reference, file)
            case 2: self.showConstellation(file)
        return None
    
    def showRealistic(self, file="out.png"):
        canva = ImageMethods.create()
        for c in self.sections.values():
            for s in reversed(c.set.values()):
                if not s.visivel: continue
                if not 0 <= s.posX < 1572: continue
                if not 0 <= s.posY < 1572: continue
                r, g, b = ColorMethods.hex_to_tuple(s.rgb_estrela)
                ImageMethods.drawCircle(canva, s.posX, s.posY, s.tamanho, r, g, b)
        canva.save(f"{os.path.dirname(__file__)}/out.png")
    
    def showDesignation(self, reference, file="out.png"):
        canva = ImageMethods.create()
        for c in self.sections.values():
            for s in reversed(c.set.values()):
                if not s.visivel: continue
                if not 0 <= s.posX < 1572: continue
                if not 0 <= s.posY < 1572: continue
                if reference == c.index:
                    r, g, b = ColorMethods.hex_to_tuple(s.rgb_designacao)
                else:
                    r, g, b = ColorMethods.hex_to_tuple("FFFFFF")
                ImageMethods.drawCircle(canva, s.posX, s.posY, s.tamanho, r, g, b)
        canva.save(f"{os.path.dirname(__file__)}/out.png")
    
    def showConstellation(self, file="out.png"):
        canva = ImageMethods.create()
        for c in self.sections.values():
            c.color()
            for s in reversed(c.set.values()):
                if not s.visivel: continue
                if not 0 <= s.posX < 1572: continue
                if not 0 <= s.posY < 1572: continue
                r, g, b = ColorMethods.hex_to_tuple(s.rgb_designacao)
                ImageMethods.drawCircle(canva, s.posX, s.posY, s.tamanho, r, g, b)
        canva.save(f"{os.path.dirname(__file__)}/out.png")

    def printPage(self, R: list, filename:str = "out.png"):
        canva = ImageMethods.create()
        for c in self.sections.values():
            c.color()
            for s in reversed(c.set.values()):
                s: Star
                s.rotate(R)
                if not s.visivel: continue
                if not 0 <= s.posX < 1572: continue
                if not 0 <= s.posY < 1572: continue
                r, g, b = ColorMethods.hex_to_tuple(s.rgb_designacao)
                ImageMethods.drawCircle(canva, s.posX, s.posY, s.tamanho, r, g, b)
        canva.save(f"{os.path.dirname(__file__)}/{filename}")
        return None



if __name__ == "__main__":
    database = f"{os.path.dirname(__file__)}/database"
    with open(f"{database}/stars.csv", "r") as ifile:
        estrelasDB = Table(ifile)
    with open(f"{database}/constellations.csv", "r") as ifile:
        constelacoesDB = Table(ifile)
    
    uranographia = Uranographia()

    for c in constelacoesDB.li:
        uranographia.subdivide(Constellation(index   = int(c[0]),
                                             nome    = c[1],
                                             sigla   = c[2],
                                             R       = c[3:12],
                                             rgb     = c[12]))
    for e in estrelasDB.li:
        uranographia.populate(int(e[1]),
                              Star(index            = int(e[0]),
                                   x                = float(e[13]),
                                   y                = float(e[14]),
                                   z                = float(e[15]),
                                   rgb_estrela      = e[7],
                                   rgb_designacao   = e[8],
                                   designacao       = e[3],
                                   magnitude        = float(e[5])
                              ))
    
    pages = [[[1,0,0],[0,0,1],[0,-1,0]],
             [[0.5,0.866025403784,0],[0,0,1],[0.866025403784,-0.5,0]],
             [[0.5,-0.866025403784,0],[0,0,1],[-0.866025403784,-0.5,0]],
             [[1,0,0],[0,0,1],[0,-1,0]],
             [[0.5,0.866025403784,0],[0,0,1],[0.866025403784,-0.5,0]],
             [[0.5,-0.866025403784,0],[0,0,1],[-0.866025403784,-0.5,0]],
             [[0.57735026919,0.57735026919,0.57735026919],[-0.707106781187,0,0.707106781187],[0.408248290464,-0.816496580928,0.408248290464]],
             [[0.57735026919,-0.57735026919,-0.57735026919],[0.707106781187,0,0.707106781187],[-0.408248290464,-0.816496580928,0.408248290464]],
             [[0.57735026919,0.57735026919,-0.57735026919],[0.707106781187,0,0.707106781187],[0.408248290464,-0.816496580928,-0.408248290464]],
             [[0.57735026919,-0.57735026919,0.57735026919],[-0.707106781187,0,0.707106781187],[-0.408248290464,-0.816496580928,-0.408248290464]],
             [[0.57735026919,0.57735026919,-0.57735026919],[0.707106781187,0,0.707106781187],[0.408248290464,-0.816496580928,-0.408248290464]],
             [[0.57735026919,-0.57735026919,0.57735026919],[-0.707106781187,0,0.707106781187],[-0.408248290464,-0.816496580928,-0.408248290464]],
             [[0.57735026919,0.57735026919,0.57735026919],[-0.707106781187,0,0.707106781187],[0.408248290464,-0.816496580928,0.408248290464]],
             [[0.57735026919,-0.57735026919,-0.57735026919],[0.707106781187,0,0.707106781187],[-0.408248290464,-0.816496580928,0.408248290464]],
             [[0,0,1],[-1,0,0],[0,-1,0]],
             [[0,0,-1],[1,0,0],[0,-1,0]]]
    for c, page in enumerate(pages):
        uranographia.printPage(page, f"{c + 16}.png")