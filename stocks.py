#CS175L-50
#Antonio Vinagre
#stocks.py

commission_rate = input("What was the commission rate for the stocks? ")
num_shares = input("How many were purchased? ")
purchase_price = input("How much was the purchase price? ")
selling_price = input("How much did you sell them for? ")


amountPaidForStock = float(num_shares) * float(purchase_price)
purchaseCommission = float(commission_rate) * amountPaidForStock

totalPaid = amountPaidForStock + purchaseCommission

soldStockFor = float(num_shares) * float(selling_price)
sellingCommission = float(commission_rate) * soldStockFor

totalReceived = soldStockFor - sellingCommission

profitOrLoss = totalReceived - totalPaid

totalCommission = purchaseCommission + sellingCommission

print(f"Joe paid ${amountPaidForStock:,.2f} for the stocks.")
print(f"He paid ${purchaseCommission:,.2f} in commission when buying the stocks.")
print(f"He then sold the stock for ${soldStockFor:,.2f}.")
print(f"He paid the broker ${sellingCommission:,.2f} after recieving the stock.")
print(f"He made ${totalReceived:,.2f} off of the sale.")
print(f"The total commission he paid was ${totalCommission:,.2f}.")
print(f"And finally, he profitted ${profitOrLoss:,.2f} at the end.")
