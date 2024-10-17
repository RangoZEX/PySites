# **PySites**

> _A simple and stylish animated website built with Flask._  
> This project serves as the homepage for **AMC Dev**, featuring **cool animations**, a **live clock**, and a redirect to **AMC Dev's** [Telegram group](https://t.me/amcdev).

---

## **✨ Installation & Setup**

_To run **PySites** locally, follow these steps:_

### 1. **Clone the repository:**
`git clone https://github.com/RangoZex/PySites.git
cd PySites`

### 2. **Install dependencies:**

`pip install -r requirements.txt`

### 3. **Configure environment variables:**
> Create a .env file in the root directory with the following content:

`BASE_URL=your-heroku-app-url`

### 4. **Run the application:**
`python app.py`



## **🛠️ Tech Stack**

```mermaid
graph TD;
    A[Frontend] -->|uses| B[HTML];
    A -->|uses| C[CSS];
    A -->|uses| D[JavaScript];
    E[Backend] -->|uses| F[Flask];
    G[Database] -->|uses| H[SQLite];
    I[Hosting] -->|uses| J[Heroku];
