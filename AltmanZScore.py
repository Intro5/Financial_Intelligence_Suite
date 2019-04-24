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

    def calcAltmanZScore():
        return 1.2*a + 1.4*b + 3.3*c + 0.6*d + e # calculate and return Altman Z-Score
