import mysql.connector
from mysql.connector import Error
<<<<<<< Updated upstream
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
=======

def create_database():
    """Create the student_db database if it doesn't exist"""
    try:
        # Connect to MySQL server (without specifying database)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='Samsimi@123'  # Replace with your MySQL password
>>>>>>> Stashed changes
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS intelligent_conversational_ai_db")
            print("Database 'intelligent_conversational_ai_db' created successfully!")
            
            # Use the database
            cursor.execute("USE intelligent_conversational_ai_db")
            
<<<<<<< Updated upstream
            # Create table
            create_table_query = """
            CREATE TABLE IF NOT EXISTS conversational_entities (
                id INT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INT NOT NULL,
                grade VARCHAR(50) NOT NULL
=======
            # Create entities table
            create_table_query = """
            CREATE TABLE IF NOT EXISTS conversational_entities (
                id INT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT NOT NULL,
                grade VARCHAR(10) NOT NULL
>>>>>>> Stashed changes
            )
            """
            cursor.execute(create_table_query)
            print("Table 'conversational_entities' created successfully!")
            
    except Error as e:
        print(f"Error: {e}")
<<<<<<< Updated upstream
    
=======
>>>>>>> Stashed changes
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()