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
    def calcWACC(self):
        return pFe * re + pDe * rd * (1 - tC) # calcualte and return WACC

        
# This class calculates the capital asset pricing model or "CAPM"
class CAPM:

    # constructor
    def __init__(self, rf = 0, bi = 0, eRm = 0, ppec = 0, ppep = 0, d = 0):
        self.rf = rf # Risk-free rate
        self.bi = bi # Beta of the investment
        self.eRm = eRm # Expected return of market
        self.ppec = ppec # Current Period Property and Equipment
        self.ppep = ppep # Prior Period Property and Equipment
        self.d = d # depreciation from the current period

    def calcCAPM(self):
        # (eRm - rf) market risk premium
        return rf + bi * (eRm - rf) # use CAPM model to caluclate and return "Expected return of investment"

    def calcCapEX(self):
        return ppec - ppep + d # calculate and return capex "Capital Expendatures"


# calculate the Altman Z-Score
# note this is best used for companies engaged in some form of manufacturing
class AltmanZScore:

    # constructor
    def __init__(self, wc = 0, ta = 0, re = 0, ebit = 0, mve = 0, tl = 0, s = 0):
        self.wc = wc # working capital
        slef.ta = ta # total assets
        self.re = re # retained earnings
        self.ebit = ebit # earnings before interest and tax
        self.mve = mve # market value of equity
        self.tl = tl # total liabilities
        self.s = s # sales

    a = wc / ta # calcualte A "working capital / total assets"
    b = re / ta # calcualte B "retained earnings / total assets"
    c = ebit / ta # calcualte C "earnings before interest and tax / total assets"
    d = mve / tl # calcualte D "market value of equity / total liabilities"
    e = s / ta # calcualte E "sales / total assets"

    def calcAltmanZScore(self):
        return 1.2*a + 1.4*b + 3.3*c + 0.6*d + e # calculate and return Altman Z-Score

class EV:

    def __init__(self, mcap = 0, td = 0, cash = 0):
        self.mcap = mcap # market capitalization
        self.td = td # total debt
        self.cash = cash # cash

# a class to caluclate EBITDA
class EBITDA:

    def __init__(self, np = 0, i = 0, t = 0, d = 0, a = 0):
        self.np = np # net profit
        self.i = i # interest
        self.t = t # taxes
        self.d = d # depreciation
        self.a = a # amortization

    def calcEBITDA(self):
        return np + i + t + d + a # calcualte and return EBITDA
