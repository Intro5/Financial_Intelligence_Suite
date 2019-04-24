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

    def calcCAPM():
        # (eRm - rf) market risk premium
        return rf + bi * (eRm - rf) # use CAPM model to caluclate and return "Expected return of investment"

    def calcCapEX():
        return ppec - ppep + d # calculate and return capex "Capital Expendatures"
