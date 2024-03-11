import sqlite3

def print_all_details():
    # Connect to the database
    conn = sqlite3.connect('userdetails.db')
    cursor = conn.cursor()

    # Execute the SQL query to select all rows from the table
    cursor.execute("SELECT * FROM details")

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Print the details
    for row in rows:
        print(row)

    # Close the database connection
    conn.close()

# Example usage
print_all_details()