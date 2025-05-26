if __name__ == '__main__':
	
    import sqlite3

    connection = sqlite3.connect('data/users.db')
    cursor = connection.cursor()
    
    with open('data/schema.sql', 'r') as f:
        cursor.executescript(f.read())

    connection.commit()
    connection.close()
    
    from load.connect import Connect
    bot = Connect()
    bot.run()