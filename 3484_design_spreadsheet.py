class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0 for i in range(26)] for j in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0])-65
        row = int(cell[1:]) - 1
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0])-65
        row = int(cell[1:])-1
        self.grid[row][col] = 0

    def getValue(self, formula: str) -> int:
        cells = formula[1:].split("+")
        res = 0
        for cell in cells:
            if cell[0].isnumeric():
                res += int(cell)
            else:
                col = ord(cell[0])-65
                row = int(cell[1:]) - 1
                res += self.grid[row][col]
        return res


obj = Spreadsheet(24)
obj.setCell("B24", 66688)
obj.resetCell("O15")
