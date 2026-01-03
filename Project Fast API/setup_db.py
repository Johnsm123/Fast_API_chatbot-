import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Samsimi@123'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS intelligent_conversational_ai_db")
            print("Database 'intelligent_conversational_ai_db' created successfully!")
            
            # Use the database
            cursor.execute("USE intelligent_conversational_ai_db")
            
            # Create table
            create_table_query = """
            CREATE TABLE IF NOT EXISTS conversational_entities (
                id INT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INT NOT NULL,
                grade VARCHAR(50) NOT NULL
            )
            """
            cursor.execute(create_table_query)
            print("Table 'conversational_entities' created successfully!")
            
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()