# FastAPI CRUD Application

This is a simple CRUD (Create, Read, Update, Delete) application built with FastAPI and SQLAlchemy. It serves as a template for building RESTful APIs with Python.

## Project Structure

```
fastapi-crud-app
├── app
│   ├── main.py          # Entry point of the application
│   ├── models.py        # Database models
│   ├── schemas.py       # Pydantic schemas for data validation
│   ├── crud.py          # CRUD operations
│   ├── database.py      # Database connection and session management
│   └── api
│       └── routes.py    # API routes
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-crud-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

- **Create**: `POST /items/`
- **Read**: `GET /items/` and `GET /items/{id}`
- **Update**: `PUT /items/{id}`
- **Delete**: `DELETE /items/{id}`

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.