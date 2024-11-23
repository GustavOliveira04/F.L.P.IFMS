# stocks = {
#     "AAPL": (150.0, 140.0, 160.0),
#     "GOOG": (1235.20, 1242.54, 1231.06),
#     "MSFT": (110.41, 110.45, 109.84),
#     "FB": (177.46, 178.67, 175.79),
# }

# >>> stocks["GOOG"]
# (1235.20, 1242.54, 1231.06)
# >>> stocks["RIM"]
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# KeyError: 'RIM'
# >>> print(stocks.get("RIM"))
# None
# >>> stocks.get("RIM", "NOT FOUND")
# 'NOT FOUND'
# >>> stocks.setdefault("GOOG", "INVALID")
# (613.3, 625.86, 610.5)
# >>> stocks.setdefault("BBRY", (10.87, 10.76, 10.90))
# (10.50, 10.62, 10.39)
# >>> stocks["BBRY"]
# (10.50, 10.62, 10.39)
# >>> stocks["GOOG"] = (1245.21, 1252.64, 1245.18)
# >>> stocks["GOOG"]
# (1245.21, 1252.64, 1245.18)
# >>> del stocks["GOOG"]
# >>> stocks["GOOG"]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'GOOG'