from account import Account


acc = Account('Linus', 'Torvalds', 'MST')

t = acc.deposit(100)

print(acc.balance)
print(t)

t2 = acc.withdraw(20)
print(t2)
print(acc.balance)

t3 = acc.deposit_rate()
print(t3)
print(acc.balance)

t4 = acc.withdraw(5000)
print(t4)
print(acc.balance)

