
# Cafe Web App

A full-stack application for managing cafes and their employees, built with FastAPI (backend) and a modern JavaScript frontend.

## 🚀 Main Features

- **Cafe & Employee Management:** Easily add, edit, and delete cafes and employees.
- **Advanced Filtering:**  
  - Filter cafes by location.
  - Filter employees by cafe name.  
  *(New in v1.0!)*
- Simple and intuitive UI for efficient management.

---

## 🛠️ Installation & Local Deployment

### 1. Clone the Repository

```bash
git clone https://github.com/arnavbajpai/Cafe-web-app.git
cd Cafe-web-app
```

### 2. Set Up the Database

- Copy the provided MySQL schema and create a database in MySQL.

### 3. Save MySQL Connection Password as Environment Variable

Replace `<your_mysql_password>` with your actual MySQL password:

**On Linux/macOS:**
```bash
export MY_SQL_PASSWORD="<your_mysql_password>"
```

**On Windows (Command Prompt):**
```cmd
set MY_SQL_PASSWORD=<your_mysql_password>
```

**On Windows (PowerShell):**
```powershell
$env:MY_SQL_PASSWORD="<your_mysql_password>"
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

- Open a new terminal window.
- Navigate to the frontend directory:

```bash
cd frontend
```

- Install dependencies:

```bash
npm install
```

### 7. Run the Frontend Server

```bash
npm run dev
```

---

## 🌐 Deployed App

**Live Link:** (TBD)

---

## 📂 Project Structure

- `main.py` - FastAPI backend entrypoint
- `frontend/` - Frontend React/Vue/JS application

- Additional directories/files for configuration and utilities

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome! Please open an issue to discuss potential changes.

---

## 📄 License

This project is licensed under the MIT License.

---

*For any issues or questions, please contact [arnavbajpai](https://github.com/arnavbajpai).*
