
# 🐍 Snakebite Antidote Prediction System

This repository contains the implementation of a **Snakebite Antidote Prediction System** developed using the **Django web framework**. The project is part of a health-tech initiative that assists medical professionals in identifying appropriate antidotes based on user inputs such as snake type, symptoms, and severity level.

---

## 📌 Project Objective
To build a web-based application that:
- Predicts the most suitable antidote for a given snakebite scenario.
- Provides users with intuitive input forms and real-time prediction.
- Supports medical aid in rural or emergency settings using minimal infrastructure.
- Leverages **CNN (Convolutional Neural Networks)** for better accuracy in severity prediction based on input features.

---

## ⚙️ Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, Bootstrap
- **Database**: SQLite
- **Machine Learning**:  
  - scikit-learn (initial model)  
  - **CNN (Convolutional Neural Network)** implemented using TensorFlow/Keras for severity level prediction

---

## 🚀 Features
- User-friendly **web interface** for entering snakebite details
- Displays relevant **antidote information** instantly
- Fully responsive and **mobile-friendly design**
- **CNN-based model** for more accurate severity prediction
- Modular Django structure for scalability and maintenance

---

## 🏁 How to Run This Project

### 🔧 Setup Instructions
```bash
# 1. Clone the repository
https://github.com/kaushal354/snakebite-kaushal.git

# 2. Navigate into the project directory
cd snakebite-kaushal

# 3. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Start the server
python manage.py runserver
```

### 🌐 Access the app
Visit: `http://127.0.0.1:8000/`

---

## 📁 Project Structure
```
snakebite-kaushal/
├── snakebite/            # Main Django app
│   ├── templates/        # HTML templates
│   ├── static/           # CSS, JS files
│   ├── views.py          # Business logic
│   ├── cnn_model/        # CNN model files (Keras/TensorFlow)
│   └── urls.py           # URL routing
├── manage.py
├── db.sqlite3            # Default database
└── requirements.txt
```

---

## 📷 Screenshots
> _Coming Soon_: Add screenshots of your homepage, prediction result, and form page.

---

## 🧠 Future Scope
- Expand the **CNN model** with more training data for better prediction
- Support for **voice-input** or offline detection
- Add real-world dataset for enhanced accuracy
- Deploy on cloud (Render, Railway, Heroku, etc.)

---

## 👨‍💻 Author
**Kaushal Prasad**  
> B.Tech CSE Student, Parul University  
> Developed during health-tech innovation sprint.

---

## 📝 License
This project is open-source and available for academic use.

---

**Feel free to fork, improve, and contribute!**
