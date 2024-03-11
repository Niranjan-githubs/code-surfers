import sqlite3

def create_table():
    conn = sqlite3.connect('userdetails.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS details (
                        ID INTEGER PRIMARY KEY,
                        NAME TEXT NOT NULL,
                        PASSWORD TEXT NOT NULL,
                        PRIVILEGE TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def recreate_table():
    conn = sqlite3.connect('userdetails.db')
    cursor = conn.cursor()

    cursor.execute('''DROP TABLE IF EXISTS details''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS details (
                        ID INTEGER PRIMARY KEY,
                        NAME TEXT NOT NULL,
                        PASSWORD TEXT NOT NULL,
                        PRIVILEGE TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Call the function to recreate the table
recreate_table()

def validate_input(username, password):
    if not username:
        print("Username cannot be empty.")
        return False
    if not password:
        print("Password cannot be empty.")
        return False
    return True

def add_user_details():
    # Prompt the user for input
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    privilege = input("Enter the privilege level (admin/user): ")

    # Validate input
    if not validate_input(username, password):
        return False

    # Connect to the database
    conn = sqlite3.connect('userdetails.db')
    cursor = conn.cursor()

    # Insert the user details into the database
    cursor.execute("INSERT INTO details (NAME, PASSWORD, PRIVILEGE) VALUES (?, ?, ?)", (username, password, privilege))
    conn.commit()

    # Close the database connection
    conn.close()

    return True

# Example usage
if add_user_details():
    print("User details added successfully!")