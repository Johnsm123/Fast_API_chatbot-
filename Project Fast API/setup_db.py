from sqlalchemy import create_engine, Column, Integer, String
from database import create_tables

            host='localhost',
        connection = mysql.connector.connect(
            
            # Create table
            create_table_query = """
            cursor.execute(create_table_query)
    except Error as e:
def main():
    print("Creating database tables...")
    create_tables()
    print("Database tables created successfully!")

if __name__ == "__main__":
    main()