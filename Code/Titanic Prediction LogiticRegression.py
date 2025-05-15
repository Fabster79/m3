import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Daten laden
file_path = 'Titanic Dataset.csv'
data = pd.read_csv(file_path)

# Datenvorbereitung
# Relevante Spalten auswählen und fehlende Werte entfernen
data = data[['age', 'sex', 'pclass', 'survived']].dropna()

# Label-Encoding für Geschlecht
label_encoder = LabelEncoder()
data['sex'] = label_encoder.fit_transform(data['sex'])  # 0 = female, 1 = male

# Features und Zielvariable definieren
X = data[['age', 'sex', 'pclass']]
y = data['survived']

# Trainings- und Testdaten aufteilen
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelltraining
model = LogisticRegression()
model.fit(X_train, y_train)

# Modellbewertung
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix)

class_report = classification_report(y_test, y_pred)
print("Classification Report:\n", class_report)

# Vorhersagefunktion
def predict_survival(age, sex, pclass):
    # Sex umwandeln in numerisches Format
    sex_encoded = 0 if sex.lower() == 'female' else 1
    # Daten in das Modell eingeben
    input_data = pd.DataFrame([[age, sex_encoded, pclass]], columns=['age', 'sex', 'pclass'])
    prediction = model.predict(input_data)[0]
    result = 'Überlebt' if prediction == 1 else 'Nicht überlebt'
    print(f"Vorhersage: {result}")

# Beispielvorhersage

predict_survival(25, 'female', 1)
