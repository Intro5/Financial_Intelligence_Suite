from IntrinioAPIStandardizedFinancials import FundamentalData
import pandas as pd

new_FinancialData = FundamentalData('AAPL', 2018)
new_FinancialData.getFinancialData()
# balance_sheet_statement_DF = pd.DataFrame(list(new_FinancialData.balance_sheet_statement.items()), columns=['LineItem', 'Value'])
# income_statement_DF = pd.DataFrame(list(new_FinancialData.income_statement.items()), columns=['LineItem', 'Value'])
# cash_flow_statement_DF = pd.DataFrame(list(new_FinancialData.cash_flow_statement.items()), columns=['LineItem', 'Value'])
# calculations_DF = pd.DataFrame(list(new_FinancialData.calculations.items()))

# pd.options.display.max_rows = 130
# print(balance_sheet_statement_DF)
# print(income_statement_DF)
# print(cash_flow_statement_DF)
print(new_FinancialData.calculations)
