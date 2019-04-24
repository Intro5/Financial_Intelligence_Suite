from IntrinioAPIGetStockPriceData import StockData


new_StockData = StockData("AAPL", 300)
print(new_StockData.identifier)
new_StockData.getStockData()
#print(*new_StockData.correspondingDates[0])
print(new_StockData.priceData[0])

# new_StockData2 = StockData("HAL", 10)
# print(new_StockData2.identifier)
# new_StockData2.getStockData()
# print(*new_StockData2.correspondingDates)
# print(*new_StockData2.priceData)
