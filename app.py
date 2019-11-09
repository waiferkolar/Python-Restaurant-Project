import eel
from help import *
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()


eel.init("web")


def insertTable(name):
    new_table = Table(name=name)
    session.add(new_table)
    session.commit()
    lisy = []
    tables = session.query(Table).all()
    for row in tables:
        lisy.append([row.id, row.name])
    return lisy


@eel.expose
def getAllTable():
    lisy = []
    tables = session.query(Table).all()
    for row in tables:
        lisy.append([row.id, row.name])

    print(lisy)
    return lisy


def insertDish(name, price):
    new_dish = Dish(name=name, price=price)
    session.add(new_dish)
    session.commit()


def getAllDish():
    return session.query(Dish).all()


def insertOrder(table_id, dish_id, dish_count):
    new_order = Order(table_id=table_id, dish_id=dish_id,
                      dish_count=dish_count)
    session.add(new_order)
    session.commit()


def getAllOrder():
    return session.query(Order).all()


def getOrderByTableId(table_id):
    return session.query(Order).filter(Order.table_id.like(table_id))


def getOrderByTableAndDishId(table_id, dish_id):
    return session.query(Order).filter(Order.table_id.like(table_id)).filter(Order.dish_id.like(dish_id))

eel.start("index.html")
