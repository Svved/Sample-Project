# SIMPLE EXAMPLE PROJECT

## OBJECTIVE

The objective of this repository is to create a model based on medical data and implement a client/server web interface using Flask to allow for predictions to be made based on the created model.

## DESCRIPTION

The data relates to pregnant patients and the presence or absence of the "placenta previa" pathology. Placenta previa is a condition in which the placenta attaches to the lower part of the uterus, partially or totally covering the internal cervical os. It affects about 1% of pregnancies and is associated with a risk of antepartum hemorrhage, preterm birth, cesarean section, and complications for both mother and fetus. The available dataset describes the clinical records of pregnant patients and whether they developed placenta previa.

## THE DATASET IS IN JSON FORMAT AND CONTAINS THE FOLLOWING COLUMNS:

1.  Age
2.  NumberOfPreviousPregnancies
3.  NumberOfPreviousCesareanSections
4.  PreviousPlacentaPrevia (0 or 1)
5.  SecondTrimesterBleeding (0 or 1)
6.  TwoHourSerumInsulin (microunits per milliliter of blood)
7.  BodyMassIndex (weight in kilograms divided by the square of the height in meters)
8.  AssistedFertilization (0 or 1)
9.  PatientAffectedByPlacentaPrevia (0 or 1 -> target column)

## SEQUENCE

1.  Load the JSON data and check for any missing data, outliers, or inconsistencies. Replace missing/anomalous data.
2.  Calculate descriptive statistics (mean, median, standard deviation) for the variables.
3.  Analyze correlations to find the variables most associated with placenta previa.
4.  Encode any categorical variables and Normalize/Standardize numerical variables.
5.  Split the data into training/testing sets (80%/20%).
6.  Choose a classification algorithm and perform a search for the best parameters.
7.  Evaluate the final model and create a `PredictPlacentaPrevia(...)` function that takes the variables as input and returns the prediction (0 or 1) and the probability.
8.  Implement a Web API with a `/predict` endpoint that accepts a POST request with the patient's data in JSON (raw json), calls the `PredictPlacentaPrevia(...)` function, and returns the data in JSON.
9.  Create a web page (HTML + JavaScript) to enter the patient's data. Add a button to send the data to the Flask endpoint via an AJAX/fetch API call. Display the prediction (probability of placenta previa) on the page.

## Project Usage

This section provides instructions on how to set up and run the project, and how to use its different components.

### Prerequisites

*   Python 3.8 or higher
*   pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd repository-name
    ```

2.  **Create a virtual environment (recommended):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**

    A `requirements.txt` file should be created to list all the necessary libraries.

### Running the Application

Once the dependencies are installed, you can start the Flask web server.

1.  **Navigate to the `src` directory:**
    ```sh
    cd src
    ```

2.  **Run the Flask application:**
    ```sh
    python app.py
    ```
    The application will start on `http://127.0.0.1:5000`.

## API Endpoints

The application provides a RESTful API for making predictions.

### /predict

*   **Method:** `POST`
*   **Description:** Receives patient data in JSON format and returns a prediction for the risk of placenta previa.
*   **Request Body:** A JSON object containing the patient's data.

    **Example Request Body:**
    ```json
    {
        "Eta": 25,
        "NumeroGravidanzePregresse": 2,
        "NumeroTagliCesareiPregressi": 2,
        "PrecedentePlacentaPrevia": 1,
        "SanguinamentiNelSecondoTrimestre": 1,
        "InsulinaSiericaDueOre": 110,
        "IndiceDiMassaCorporea": 32.5,
        "FecondazioneAssisitita": 0
    }
    ```

*   **Response:** A JSON object containing the prediction and the probability of having placenta previa.

    *   `prediction`: `1` if the risk is high, `0` if the risk is low.
    *   `probability`: The probability of the positive class (placenta previa), as a float between 0 and 1.

    **Example Response:**
    ```json
    {
        "prediction": 1,
        "probability": 0.6275
    }
    ```

## Web Interface

The project includes a simple web interface to interact with the prediction model.

### How to Use

1.  **Open your web browser** and navigate to `http://127.0.0.1:5000`.
2.  **Fill in the form** with the patient's data. All fields are required.
3.  **Click the "Calcola Rischio" (Calculate Risk) button.**
4.  The prediction result will be displayed below the button, showing the probability of placenta previa and a final outcome (e.g., "POSITIVE (High Risk)" or "NEGATIVE (Low Risk)").