from currency_converter import CurrencyConverter
print("this is a currecy converter project")
print("you can use these currency ('INR','USD','EUR'.'JPY')")
amount=float(input(print("enter the amount you want to convert: ")))
cu_currency=input("enter the currency which you currently have :")
want_currency=input("enter the currency you want to have : ")
c=CurrencyConverter()
coverted_amount=c.convert(amount,cu_currency,want_currency)
print(f"The {amount} {cu_currency}in {want_currency} is: { coverted_amount}")

