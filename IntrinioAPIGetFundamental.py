from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OjlmODA4ZTJjZTQ0ZTIxNTUyYmZjNDY5NTc2MWNmY2Q0'

fundamentals_api = intrinio_sdk.FundamentalsApi()

identifier = 'AAPL' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
statement_code = 'balance_sheet_statement' # str | The statement code
fiscal_year = 2016 # int | The fiscal year
fiscal_period = 'FY' # str | The fiscal period

try:
    api_FundamentalResponse = fundamentals_api.lookup_fundamental(identifier, statement_code, fiscal_year, fiscal_period).__dict__
    print(api_response['_id'])
except ApiException as e:
    print("Exception when calling FundamentalsApi->lookup_fundamental: %s\n" % e)
