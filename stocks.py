#CS175Lab-50
#Antonio Vinagre
#stocks.py

commission_rate = float(input("What was the commission rate?: "))
num_shares = float(input("How many shares did you purchase?: "))
purchase_price = float(input("What was the purchase price?: "))
selling_price = float(input("What was the selling price?: "))


amountPaidForStock = num_shares * purchase_price
purchaseCommission = commission_rate * amountPaidForStock

totalPaid = amountPaidForStock + purchaseCommission

soldStockFor = num_shares * selling_price
sellingCommission = commission_rate * soldStockFor

totalReceived = soldStockFor - sellingCommission

profitOrLoss = totalReceived - totalPaid

totalCommission = purchaseCommission + sellingCommission

print(f"Amount Paid for Stock: ${amountPaidForStock:,.1f}")
print(f"Commission Paid on the Purchase: ${purchaseCommission:,.1f}")
print(f"Amount the Stock Sold for: ${soldStockFor:,.1f}")
print(f"Commission Paid on the Sale: ${sellingCommission:,.1f}")
print(f"Total Commission Paid: ${totalCommission:,.1f}")
print(f"Profit (or Loss, if Negative): ${profitOrLoss:,.1f}")
