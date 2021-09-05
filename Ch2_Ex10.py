Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> sugar_48_cookies = 1.5 # cups
>>> butter_48_cookies = 1 # cups
>>> flour_48_cookies = 2.75 # cups
>>> num_cookies = int(input("How many cookies do you want to make> "))
How many cookies do you want to make> 12
>>> sugar_amount = (sugar_48_cookies / 48) * num_cookies
>>> butter_amount = (butter_48_cookies / 48) * num_cookies
>>> flour_amount = (flour_48_cookies / 48) * num_cookies
>>> print("You will need the following amounts: ")
You will need the following amounts: 
>>> print(format(sugar_amount, '.2f'), "cups of sugar")
0.38 cups of sugar
>>> print(format(butter_amount, '.2f'), "cups of butter")
0.25 cups of butter
>>> print(format(flour_amount, '.2f'), "cups of flour")
0.69 cups of flour
>>> 
