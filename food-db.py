import sqlite3

conn = sqlite3.connect('food_database.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS food (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        ingredients TEXT NOT NULL,
        description TEXT
    )
''')

def insert_food(food_tuple):
    cursor.execute('''
        INSERT INTO food (name, ingredients, description) VALUES (?, ?, ?)
    ''', food_tuple)
    conn.commit()

food_tuples = [
    ("Spaghetti Carbonara", "Pasta, Eggs, Pancetta, Parmesan Cheese, Black Pepper", "A classic Italian pasta dish."),
    ("Tacos", "Tortillas, Beef, Lettuce, Cheese, Salsa", "A traditional Mexican dish."),
    ("Sushi", "Rice, Fish, Seaweed, Soy Sauce", "A Japanese dish consisting of vinegared rice and seafood.")
]

for food in food_tuples:
    insert_food(food)

def fetch_all_foods():
    cursor.execute('SELECT * FROM food')
    return cursor.fetchall()

foods = fetch_all_foods()
for food in foods:
    print(f"ID: {food[0]}, Name: {food[1]}, Ingredients: {food[2]}, Description: {food[3]}")

conn.close()