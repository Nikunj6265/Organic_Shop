from app.models import Customer, Cart, Product, OrderePlaced
from django.contrib.auth.models import User
from django.db import connection
def run():
    product1 = Customer.objects.all().values().first()
    # for p in product:
    #     print(p.user)
    print(product1)
    
    
    
    print(connection.queries)
"""
OUTPUT 
PS C:\SHOPPINGLYX\shoppinglyx> python manage.py runscript orm_script
Nikunj Gour
roahn
PS C:\SHOPPINGLYX\shoppinglyx> python manage.py runscript orm_script
roahn
roahn patidar
"""