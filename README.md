# FastAPI Project
This project is a RESTful API built using FastAPI, following the Model-View-Controller (MVC) architecture. It provides endpoints for managing plans, permissions, users, subscriptions, and usage.

## Features
- Create, read, update, and delete (CRUD) operations for plans, permissions, users, and subscriptions.
- Built with FastAPI for high performance and automatic API documentation.
- Uses SQLAlchemy for database interactions with a MySQL backend.

## Technologies Used
- **FastAPI**: A modern web framework for building APIs with Python.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) system for Python.
- **MySQL**: A popular relational database management system.

## Setup Instructions
1. **Clone the repository**:  
   ```bash
   git clone <repository-url>
   cd my_fastapi_project

## Create a virtual environment (optional but recommended):
-python -m venv venv
-source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install the required packages:
-pip install -r requirements.txt

## Set up your MySQL database:
**Make sure you have a MySQL server running and create a database named cloud**:
CREATE DATABASE cloud;

## Run the application:
-uvicorn app.main:app --reload

## Access the API documentation:
**Open your browser and navigate to http://localhost:8000/docs to view the automatically generated API documentation.**

# License
This project is licensed under the MIT License. See the LICENSE file for more information.
-Puedes copiar y pegar este texto directamente en tu archivo `README.md`. Si -necesitas más ajustes, no dudes en decírmelo.
