

from decimal import Decimal

num1 = Decimal('1.1')
num2 = Decimal('1.563')
num1 + num2  # Decimal('2.663')

from decimal import getcontext
ctx = getcontext()
num = Decimal('1.1')
num**4 # Decimal('1.4641')
ctx.prec = 4 # set new precision
num**4 # Decimal('1.464')



from decimal import localcontext
num = Decimal("1.1")
with localcontext() as ctx:
    ctx.prec = 2
    num**4 # Decimal('1.5')
num**4 # Decimal('1.4641')

