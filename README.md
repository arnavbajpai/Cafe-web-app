
# Cafe Web App

A full-stack application for managing cafes and their employees, built with FastAPI (backend) and a modern JavaScript frontend.

##  Main Features

- **Cafe & Employee Management:** Easily add, edit, and delete cafes and employees.
- **Search Tool:**  
  - Filter cafes by location.
  - Filter employees by cafe name.  
  *(New in v1.0!)*
- Simple and intuitive UI for efficient management.

---

##  Installation & Local Deployment

### 1. Clone the Repository

```bash
git clone https://github.com/arnavbajpai/Cafe-web-app.git
cd Cafe-web-app
```
**Note: Following assumes you have MySQL 8.0.* and python 3.9+ currently installed**
### 2. Set Up the Database

- Use the provided MySQL schema [here](/Database/dbconfig.sql) and create a database in MySQL.

### 3. Save MySQL Connection Password as Environment Variable

Replace `<your_mysql_password>` with your actual MySQL password:

**On Linux/macOS:**
```bash
export MYSQL_PASSWORD="<your_mysql_password>"
```

**On Windows (Command Prompt):**
```cmd
set MYSQL_PASSWORD=<your_mysql_password>
```

**On Windows (PowerShell):**
```powershell
$env:MYSQL_PASSWORD="<your_mysql_password>"
```

### 4. Install FastAPI and Dependencies

If FastAPI is not installed, follow the official guide:  
[FastAPI Installation Guide](https://fastapi.tiangolo.com/tutorial/)

**Quick install with pip:**
```bash
pip install fastapi "uvicorn[standard]"
```

### 5. Run the Backend Server

```bash
fastapi dev main.py
```
*Or, if using uvicorn directly:*
```bash
uvicorn main:app --reload
```

### 6. Set Up the Frontend

Refer to README of [frontend repo](https://github.com/arnavbajpai/Cafe-web-app-frontend/)

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome! Please open an issue to discuss potential changes.

---


*For any issues or questions, please contact [arnavbajpai](https://github.com/arnavbajpai).*
