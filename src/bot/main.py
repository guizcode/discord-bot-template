if __name__ == '__main__':
	
    import sqlite3

    connection = sqlite3.connect('src/bot/data/users.db')
    cursor = connection.cursor()
    
    with open('src/bot/data/schema.sql', 'r') as f:
        cursor.executescript(f.read())

    connection.commit()
    connection.close()
    
    from loader.connect import Connect
    bot = Connect()
    bot.run()