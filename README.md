# FastAPI Blog and User Management Project

## Description
This project provides a simple API for managing blogs and users. It allows you to create, delete, and update blogs in a local database directly from the project, as well as create users. All requests made can be checked at `/docs`.

<img src="https://imgur.com/RyM4ngC.png">

## Usage

### Running the Project
1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Install the required dependencies using:
    ```
    pip install -r requirements.txt
    ```
4. Run the FastAPI server with the following command:
    ```
    uvicorn main:app --reload
    ```
   This will start the server locally, and it will automatically reload whenever you make changes to the code.

### Blogs
- **Create a new blog:**  
  `POST /blogv2`
- **Delete a blog:**  
  `DELETE /blog/{id}`
- **Update a blog:**  
  `PUT /blog/{id}`
- **Retrieve all blogs:**  
  `GET /blog`
- **Retrieve a specific blog:**  
  `GET /blog/{id}`

<img src="https://imgur.com/XSUvmLc.png">

### Users
- **Create a new user:**  
  `POST /user`
- **Retrieve a specific user:**  
  `GET /user/{id}`
- **Retrieve all users:**  
  `GET /user`
- **Delete a user:**  
  `DELETE /user/{id}`

## Authentication
You can access these APIs by creating a user or using an existing one in the database:
- **Username:** test
- **Password:** test123

## Documentation
The API documentation is available at `/docs`. You can explore and interact with the endpoints directly from the provided Swagger UI.

## Author
This project was created and is maintained by Bahna Darius. You can find me on [LinkedIn](https://www.linkedin.com/in/darius-bahn%C4%83-2224b7264/).
