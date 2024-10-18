### Installation

1. **Clone the Repositary:**
```bash
git clone Starlette_Pydantic
cd Starlette_Pydantic
```

2. **Create Virtual Enviroment:**
```bash
python -m venv venv(Virtual Enviroment Name)
source venv/bin/activate  # Windows: `venv\Scripts\activate`
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
