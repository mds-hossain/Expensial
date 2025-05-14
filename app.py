
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for transactions
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)  # 'income' or 'expense'
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(50), nullable=False)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_transaction():
    if request.method == 'POST':
        type = request.form['type']
        amount = request.form['amount']
        description = request.form['description']
        category = request.form['category']
        new_transaction = Transaction(type=type, amount=float(amount), description=description, category=category)
        db.session.add(new_transaction)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    transactions = Transaction.query.all()
    total_income = sum([t.amount for t in transactions if t.type == 'income'])
    total_expenses = sum([t.amount for t in transactions if t.type == 'expense'])
    balance = total_income - total_expenses
    return render_template('dashboard.html', transactions=transactions, total_income=total_income, total_expenses=total_expenses, balance=balance)

if __name__ == '__main__':
    db.create_all()  # Creates database tables if not already present
    app.run(debug=True)
