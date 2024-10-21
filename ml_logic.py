from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

# Ajusta las rutas a tus carpetas de correos
EASY_HAM_PATH = "datasets/spamassassin/easy_ham"
HARD_HAM_PATH = "datasets/spamassassin/hard_ham"
SPAM_PATH = "datasets/spamassassin/spam_2"

# Función para cargar correos desde carpetas
def load_emails_from_folder(folder_path):
    emails = []
    for filename in os.listdir(folder_path):
        with open(os.path.join(folder_path, filename), 'r', encoding='latin-1') as f:
            emails.append(f.read())
    return emails

# Cargar correos de las tres carpetas
easy_ham_emails = load_emails_from_folder(EASY_HAM_PATH)
hard_ham_emails = load_emails_from_folder(HARD_HAM_PATH)
spam_emails = load_emails_from_folder(SPAM_PATH)

# Unir los correos ham (easy y hard) y spam
ham_emails = easy_ham_emails + hard_ham_emails
spam_labels = ['spam'] * len(spam_emails)
ham_labels = ['ham'] * len(ham_emails)

# Unir los correos y etiquetas
all_emails = spam_emails + ham_emails
all_labels = spam_labels + ham_labels

# Vectorizar los correos electrónicos utilizando TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')  # Ajustar max_features
X = vectorizer.fit_transform(all_emails)
y = all_labels

# Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluar el modelo
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))  # Reporte de clasificación
print(confusion_matrix(y_test, y_pred))  # Matriz de confusión

# Guardar el modelo y el vectorizador
joblib.dump(model, 'spam_classifier.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')


