import db

def add_item(title, description, city, user_id):
    sql = """INSERT INTO items(title,description,city,user_id) 
            VALUES (?,?,?,?)"""
    db.execute(sql, [title, description, city, user_id])