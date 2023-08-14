import psycopg2


connection = psycopg2.connect(
  host = 'localhost',
  user= 'postgres',
  password= 'taintedalpha',
  database= 'restaurant'
)

cursor = connection.cursor()

class MenuItem:
  def __init__(self, item_name, item_price):
    self.item_name = item_name
    self.item_price = item_price
  
  def __str__(self):
    return f'Your {self.item_name} is {self.item_price}'
  
  @staticmethod
  def showitems():
    cursor.execute("SELECT * FROM menu_items;")
    results = cursor.fetchall()
    for row in results:
      item = MenuItem(row[1], row[2])
      print(item)
  
  @staticmethod
  def insertItems(item_name, item_price):
    query = "INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s);"
    cursor.execute(query, (item_name, item_price))
    connection.commit()
  
  @staticmethod
  def deleteItems(item_name):
    query = "DELETE FROM menu_items WHERE item_name = %s;"
    cursor.execute(query, (item_name,))
    connection.commit()
    if cursor.rowcount > 0:
      print(f"{item_name} was deleted successfully")
    else:
      print(f"Item was not found, so it couldn't be deleted")







MenuItem.insertItems('Burger', 36)
#MenuItem.deleteItems('Burger')
MenuItem.showitems()


connection.close()