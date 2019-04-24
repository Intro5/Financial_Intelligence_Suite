# a class to caluclate EBITDA
class EBITDA:

    def __init__(self, np = 0, i = 0, t = 0, d = 0, a = 0):
        self.np = np # net profit
        self.i = i # interest
        self.t = t # taxes
        self.d = d # depreciation
        self.a = a # amortization

    def calcEBITDA():
        return np + i + t + d + a # calcualte and return EBITDA
