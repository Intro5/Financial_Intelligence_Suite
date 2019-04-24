# This is a class to calculate the Weighted Average Cost of Capital or "WACC"

class WACC:

    # re: cost of equity
    # re: cost of debt
    # e: market value of the firm's equity
    # d: market value of the firm's debt
    # v = e + d: total market value of the firm’s financing (equity and debt)
    # pFe = e/v: percentage of financing that is equity
    # pDe = d/v: percentage of financing that is debt
    # Tc: corporate tax rate

    # constructor
    def __init__(self, re = 0, rd = 0, e = 0, d = 0, tC = 0):
        self.re = re
        self.rd = rd
        self.e = e
        self.d = d
        self.tC = tC
        self.v = 0
        self.pFe = 0
        self.pDe = 0


    self.v = self.e + self.d # calcualte v "total market value of firms financing"
    self.pFe = self.e / self.v # calcualte pFe "percentage of financing that is equity"
    self.pDe = self.d / self.v # calcualte pDe "percentage of financing that is debt"

    # Get WACC
    def calcWACC():
        return pFe * re + pDe * rd * (1 - tC) # calcualte and return WACC
