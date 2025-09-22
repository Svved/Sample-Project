# librerie per applicazione Flask
from flask import Flask, request, jsonify, render_template # type: ignore
import pandas as pd # type: ignore
import joblib # type: ignore

# Caricamento del modello e dello scaler all'avvio dell'applicazione
# Definiamo i paths al miglior modello salvato e scaler etc.
model = 'models/best_model.pkl'
scaler = 'models/scaler.pkl'
try:
    model = joblib.load(model)
    scaler = joblib.load(scaler)
    print("Modello e scaler caricati con successo.")
except Exception as e:
    print(f"Errore durante il caricamento del modello o dello scaler: {e}")

def PredictPlacentaPrevia(
    Eta,
    NumeroGravidanzePregresse,
    NumeroTagliCesareiPregressi,
    PrecedentePlacentaPrevia,
    SanguinamentiNelSecondoTrimestre,
    InsulinaSiericaDueOre,
    IndiceDiMassaCorporea,
    FecondazioneAssisitita,
    model,
    scaler
):
    
    
    # È cruciale per convertire la probabilità in una previsione 0/1.
    OPTIMAL_THRESHOLD = 0.40


    # Il modello si aspetta i dati in un formato specifico (un DataFrame con i nomi delle colonne corrette).
    
    # Elenco delle colonne nell'ordine corretto in cui il modello è stato addestrato
    feature_names = [
        'Eta', 'NumeroGravidanzePregresse', 'NumeroTagliCesareiPregressi',
        'PrecedentePlacentaPrevia', 'SanguinamentiNelSecondoTrimestre',
        'InsulinaSiericaDueOre', 'IndiceDiMassaCorporea', 'FecondazioneAssisitita'
    ]

    # Crea un dizionario con i dati di input
    input_data = {
        'Eta': [Eta],
        'NumeroGravidanzePregresse': [NumeroGravidanzePregresse],
        'NumeroTagliCesareiPregressi': [NumeroTagliCesareiPregressi],
        'PrecedentePlacentaPrevia': [PrecedentePlacentaPrevia],
        'SanguinamentiNelSecondoTrimestre': [SanguinamentiNelSecondoTrimestre],
        'InsulinaSiericaDueOre': [InsulinaSiericaDueOre],
        'IndiceDiMassaCorporea': [IndiceDiMassaCorporea],
        'FecondazioneAssisitita': [FecondazioneAssisitita]
    }
    
    # Converte in DataFrame, assicurando l'ordine corretto delle colonne
    input_df = pd.DataFrame(input_data, columns=feature_names)

    # --- 4. ESECUZIONE DELLA PIPELINE DI PREDIZIONE ---
    # Step 1: Standardizzare i dati di input usando lo scaler addestrato
    input_scaled = scaler.transform(input_df)

    # Step 2: Calcolare la probabilità usando il modello addestrato
    # predict_proba restituisce le probabilità per entrambe le classi [P(0), P(1)]
    prob_all_classes = model.predict_proba(input_scaled)
    
    # Estraiamo la probabilità della classe positiva (classe 1)
    prob_positive_class = prob_all_classes[0, 1]

    # Step 3: Convertire la probabilità in una previsione finale usando la soglia ottimale
    prediction = int(prob_positive_class >= OPTIMAL_THRESHOLD)

    # --- 5. RESTITUZIONE DEI RISULTATI ---
    return prediction, prob_positive_class

app = Flask(__name__, template_folder='../templates', static_folder='../templates/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    if not model or not scaler:
        return jsonify({'error': 'Modello o scaler non sono stati caricati correttamente.'}), 500

    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'Richiesta non valida. Nessun dato JSON ricevuto.'}), 400
        
        print(f"Dati ricevuti per la predizione: {data}")

        # Chiama la funzione centralizzata "spacchettando" il dizionario dei dati
        prediction, probability = PredictPlacentaPrevia(**data, model=model, scaler=scaler)
        
        # Formatta la risposta
        response_data = {
            'prediction': prediction,
            'probability': probability
        }
        
        print(f"Risultato inviato: {response_data}")
        return jsonify(response_data)

    except TypeError as e:
        # Errore comune se i dati JSON non corrispondono agli argomenti della funzione
        print(f"Errore nei dati di input: {e}")
        return jsonify({'error': 'Dati di input non corretti o mancanti.'}), 400
    except Exception as e:
        print(f"Errore generico durante la predizione: {e}")
        return jsonify({'error': 'Si è verificato un errore interno.'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)