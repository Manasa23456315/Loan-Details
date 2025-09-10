from flask import Flask, render_template, request, redirect, url_for
from database import get_db_connection, init_db  # ✅ import init_db

# Flask app
app = Flask(__name__)  # point to your templates folder

# Initialize database at startup
init_db()

# Home page → show main loan form
@app.route('/')
def index():
    return render_template('index.html')

# Loan form routes (if you have separate forms)
@app.route('/education-loan-form')
def education_form():
    return render_template('education-loan-form.html')

@app.route('/personal-loan-form')
def personal_form():
    return render_template('personal-loan-form.html')

@app.route('/home-loan-form')
def home_form():
    return render_template('home-loan-form.html')

@app.route('/business-loan-form')
def business_form():
    return render_template('business-loan-form.html')

@app.route('/consumer-durable-loan-form')
def consumer_form():
    return render_template('consumer-durable-loan-form.html')

@app.route('/credit-card-loan-form')
def credit_form():
    return render_template('credit-card-loan-form.html')

@app.route('/gold-loan-form')
def gold_form():
    return render_template('gold-loan-form.html')

@app.route('/mortgage-loan-form')
def mortgage_form():
    return render_template('mortgage-loan-form.html')

@app.route('/vehicle-loan-form')
def vehicle_form():
    return render_template('vehicle-loan-form.html')
@app.route('/agriculture-loan-form')
def agriculture_form():
    return render_template('agriculture-loan-form.html')
@app.route('/loan-form', methods=['GET', 'POST'])
def loan_form():
    loan_type = request.args.get('loan_type', '')  # Get the loan type from URL

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        amount = request.form['amount']

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO loan_applications (name, email, loan_type, amount) VALUES (?, ?, ?, ?)",
            (name, email, loan_type, amount)  # Save loan_type from URL
        )
        conn.commit()
        conn.close()

        return redirect(url_for('index'))  # Go back to home

    return render_template('loan_form.html', loan_type=loan_type)




# View all applications
@app.route('/all_data')
def all_data():
    conn = get_db_connection()
    data = conn.execute("SELECT * FROM loan_applications").fetchall()
    conn.close()

    table = "<table border='1'><tr><th>ID</th><th>Name</th><th>Email</th><th>Loan Type</th><th>Amount</th><th>Action</th></tr>"
    for row in data:
        table += f"""
        <tr>
            <td>{row['id']}</td>
            <td>{row['name']}</td>
            <td>{row['email']}</td>
            <td>{row['loan_type']}</td>
            <td>{row['amount']}</td>
            <td>
                <a href="/delete/{row['id']}" onclick="return confirm('Are you sure you want to delete this record?');">Delete</a>
            </td>
        </tr>
        """
    table += "</table>"
    return table
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM loan_applications WHERE id = ?", (id,))
    conn.commit()
    conn.execute("DELETE FROM sqlite_sequence WHERE name='loan_applications'")
    conn.commit()
    conn.close()
    return redirect(url_for('all_data'))


if __name__ == '__main__':
    app.run(debug=True)
