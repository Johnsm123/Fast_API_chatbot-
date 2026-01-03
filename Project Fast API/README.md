# Student Management API with MySQL

A FastAPI application for managing student records with MySQL database integration.

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. MySQL Setup
- Install MySQL server on your system
- Create a MySQL user and database
- Update the `.env` file with your MySQL credentials:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=student_db
```

### 3. Initialize Database
Run the setup script to create the database and tables:
```bash
python setup_db.py
```

### 4. Run the Application
```bash
uvicorn main:app --reload
```

The API will be available at: http://localhost:8000

## API Documentation

FastAPI automatically generates interactive API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

- `GET /` - Welcome message
- `POST /students` - Create a new student
- `GET /students` - Get all students (with pagination)
- `GET /students/{student_id}` - Get student by ID
- `PUT /students/{student_id}` - Update student by ID
- `DELETE /students/{student_id}` - Delete student by ID

## Student Model

```json
{
  "id": 1,
  "name": "John Doe",
  "age": 20,
  "grade": "A"
}
```

## Features

- MySQL database integration with SQLAlchemy
- Automatic database table creation
- Input validation with Pydantic
- Error handling for duplicate IDs and missing records
- Interactive API documentation
- Environment-based configuration