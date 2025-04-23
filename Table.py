from dataclasses import dataclass
from io import TextIOBase
import os

@dataclass
class Table:
    li: list
    x: int
    y: int
    def __init__(self, file: TextIOBase):
        self.li = []
        for counter, line in enumerate(file.readlines()):
            if counter == 0: self.x = len(line.strip().split(","))
            self.li.append(line.strip().split(","))
        else:
            self.y = counter + 1
        return None
    
    def value(self, row: int, col: int):
        return self.li[row][col]
    
    def subset(self, x0: int, xn: int = 0, y0: int = 0, yn: int = 0):
        if not x0 < xn: xn = xn + self.x
        if not y0 < yn: yn = yn + self.y
        return [[x for x in y[x0:xn]] for y in self.li[y0:yn]]
    
    def subsetfloat(self, x0: int, xn: int = 0, y0: int = 0, yn: int = 0):
        if not x0 < xn: xn = xn + self.x
        if not y0 < yn: yn = yn + self.y
        return [[float(x) for x in y[x0:xn]] for y in self.li[y0:yn]]
    
    def get(self):
        return self.li

if __name__ == "__main__":
    current_folder = os.path.dirname(__file__)
    filename = f"{current_folder}/database/stars.csv"
    with open(filename, "r") as ifile:
        table = Table(ifile)
        print(table.subset(0, 5, 0, 5))
        print()
        print(table.subsetfloat(11, 16, 0, 5))
        print()
        print(f"{table.value(1360, 4)}: {float(table.value(1360, 5))}")
        print()
        print(table.get()[4754])