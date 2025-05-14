
# Expensial - Expense Tracker

## 📑 Table of Contents
1. [🧾 Introduction](#introduction)
   - Project Name
   - Project Description
   - Technologies Used
2. [✨ Features](#features)
3. [🛠️ How to Use](#how-to-use)
4. [⚙️ Installation](#installation)
5. [QA Process](#qa-process)
   - Detailed QA Process
   - Which Testing Skills and Methods Were Used
   - Results and Outcome
   - Details About the QA Directory
   - Summary
   - Conclusion
6. [📝 License](#license)

---

## 🧾 Introduction

### **Project Name**:  
**Expensial - Expense Tracker**

### **Project Description**:  
Expensial is a Python-based expense tracker application. It allows users to track their daily expenses, manage income, and view financial reports. It provides an easy-to-use web interface built with Flask, while SQLite is used for storing data.

### **Technologies Used**:  
- **Backend**: Python, Flask
- **Database**: SQLite, SQLAlchemy ORM
- **Frontend**: HTML, CSS, Bootstrap
- **Testing**: Python’s `unittest` for automated testing

---

## ✨ Features
- Add, view, edit, and delete income and expenses
- Categorize transactions (e.g., Food, Transport, Entertainment)
- Real-time financial balance update
- Dashboard displaying income vs expenses
- Export transaction history as CSV

---

## 🛠️ How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/expensial.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Visit `http://127.0.0.1:5000/` in your browser.

---

## ⚙️ Installation

1. **Clone the repository**:  
   `git clone https://github.com/yourusername/expensial.git`

2. **Install dependencies**:  
   Make sure you have Python 3.x installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**:  
   Run the application:
   ```bash
   python app.py
   ```

4. **Run the app**:  
   The app will run locally at `http://127.0.0.1:5000/`.

---

## QA Process

### Detailed QA Process:
- **Testing Skills & Methods Used**:  
  - Manual Testing: Verifying if the functionality works as expected.
  - Automated Testing: Unit testing using Python’s `unittest`.
  - Usability Testing: Ensure the UI is intuitive.
  - Load Testing: Ensuring app performance (optional).

### Results and Outcome:
- **Pass**: All major functionalities work well (add, edit, delete transactions).
- **Fail**: Minor bugs in form validation.

### QA Directory:
- `test_plan.csv`: Detailed test scenarios.
- `test_case.csv`: Specific test cases with expected outcomes.
- `bug_report.csv`: List of identified bugs.
- `test_report.csv`: Summary of test results.
- `QA_report.md`: Detailed report of QA process.

---

## 📝 License

This project is licensed under the MIT License.
