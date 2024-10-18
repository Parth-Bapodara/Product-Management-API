# Product Management API built using Pydantic and Starlette
Built a Simple Product Management API with the use of Pydantic and Starlette combining with FASTApi, which supports basic CRUD operations.

## Features
  - **Create Product**: Can create Product.
  - **Search Product**: Can search Product using ID.
  - **Delete Product**: Can delete Product. 
  - **Update Product**: Can Update Information about Product.

## Prequisites
  - **Python 3.7.0+**

## Installation

1. **Clone the Repositary:**
```bash
git clone https://github.com/Parth-Bapodara/Product-Management-API.git
cd Product-Management-API
```

2. **Create Virtual Enviroment:**
```bash
python -m venv venv(Virtual Enviroment Name)
source venv/bin/activate  # Windows: `venv\Scripts\activate' 
```

3. **Install Dependencies:**

   **For Windows or Mac:**
      ```bash
         pip install -r /path/to/requirements.txt
      ```
      ****or****
      ```bash
         python -m pip install -r /path/to/requirements.txt
      ```
   **For Linux:**
     ```bash
        sudo pip install -r requirements.txt
     ```
     
4. **Run the Application:**
   ```bash
      uvicorn main:app --reload
   ```

5. **Access the API:**
   ```bash
      Visit http://<Your Host>/docs for API documentation.
   ```
