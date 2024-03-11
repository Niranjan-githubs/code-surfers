import sqlite3

def print_all_details():
    
    conn = sqlite3.connect('userdetails.db')
    cursor = conn.cursor()

    
    cursor.execute("SELECT * FROM details")

 
    rows = cursor.fetchall()

    # Print the details
    for row in rows:
        print(row)

    
    conn.close()


print_all_details()
