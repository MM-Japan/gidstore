## ⚙️ Installation & Setup
To run GidStore locally, follow these steps:

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/MM-Japan/gidstore.git
cd gidstore
```

### **2️⃣ Set Up Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Apply Migrations**
```bash
python3 manage.py migrate
```

### **5️⃣ Create a Superuser (For Admin Panel)**
```bash
python3 manage.py createsuperuser
```

### **6️⃣ Run the Development Server**
```bash
python3 manage.py runserver
```
Now, open your browser and go to:
- **Product Listing:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

---
