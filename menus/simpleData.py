from random import randint
from django.db import transaction

def generate_sample_data():
    restaurant_names = ['The Bistro', 'Sushi Express', 'Mamma Mia Pizzeria', 'Café del Sol']
    menu_items = {
        'The Bistro': [('Grilled Salmon', 150), ('Filet Mignon', 250), ('Caesar Salad', 100)],
        'Sushi Express': [('Sushi Combo', 120), ('Sashimi Platter', 180)],
        'Mamma Mia Pizzeria': [('Margherita Pizza', 90), ('Pepperoni Pizza', 130), ('Caprese Salad', 70)],
        'Café del Sol': [('Espresso', 50), ('Cappuccino', 80), ('Croissant', 60)]
    }

    with transaction.atomic():
        for name in restaurant_names:
            restaurant = Restaurant.objects.create(name=name)
            items = menu_items.get(name, [])
            for item_name, price in items:
                MenuItem.objects.create(restaurant=restaurant, name=item_name, price=price)

    print('Generated sample data successfully')

# เรียกใช้ฟังก์ชันสร้างตัวอย่างข้อมูล
generate_sample_data()
