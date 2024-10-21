from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
import pyodbc
import joblib

# Cargar el modelo entrenado y el vectorizador
model = joblib.load('spam_classifier.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Función para analizar el correo electrónico
def analyze_email(email_data):
    text = email_data["subject"] + " " + email_data["body"]
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    
    return prediction[0] == 'spam'  # Devuelve True si es spam

app = Flask(__name__)

# Conexión a la base de datos SQL Server
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=DESKTOP-5D3IB2N\\SQLEXPRESS;'
                      'DATABASE=ProyectoML;'
                      'Trusted_Connection=yes;')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    to_address = request.form['to_address']
    subject = request.form['subject']
    body = request.form['body']
    
    email_data = {"subject": subject, "body": body}
    is_spam = analyze_email(email_data)  # True = Spam, False = Ham
    
    try:
        msg = MIMEText(body, _charset='utf-8')
        msg['Subject'] = subject
        msg['From'] = 'lleykop1996@gmail.com'
        msg['To'] = to_address

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('lleykop1996@gmail.com', 'giyn nddv jwbo jznp')
        server.sendmail('lleykop1996@gmail.com', to_address, msg.as_string())
        server.quit()

        table = 'spam' if is_spam else 'ham'
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO {table} (subject, body) VALUES (?, ?)", subject, body)
        conn.commit()

        # Devolver JSON con el resultado para el modal
        return jsonify({'is_spam': is_spam})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


