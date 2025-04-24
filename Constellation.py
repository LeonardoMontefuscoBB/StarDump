from dataclasses import dataclass
from Star import Star

@dataclass
class Constellation:
    index: int
    nome: str
    sigla: str
    R: list
    rgb : str
    set: dict
    def __init__(self, index: int, nome: str, sigla: str, R: list, rgb: str):
        assert len(R) == 9
        self.index = index
        self.nome = nome
        self.sigla = sigla
        self.R = [[float(R[row * 3 + cell]) for cell in range(3)] for row in range(3)]
        self.rgb = rgb
        self.set = {}
        return None
    
    def populate(self, s: Star, specialDesignation: str = ""):
        if specialDesignation:  self.set[specialDesignation] = s
        else:                   self.set[s.designacao] = s
        return None
    
    def color(self):
        for s in self.set.values(): s.color(self.rgb)
        return None
    

