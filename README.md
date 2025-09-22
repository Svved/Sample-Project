## OBIETTIVO

L'obiettivo di questa repo è creare un modello partendo da dati medici e implementare una interfaccia web client/server utilizzando Flask per permettere di elaborare delle previsioni basandosi sul modello creato.

## DESCRIZIONE

I dati sono relativi a delle pazienti gravide alla presenza o meno della patologia "placenta previa". La placenta previa è una condizione in cui la placenta si inserisce nella parte inferiore dell'utero, coprendo parzialmente o totalmente l'orifizio cervicale interno. Colpisce circa l'1% delle gravidanze ed è associata a rischio di sanguinamento antepartum, parto pretermine, taglio cesareo e complicanze per madre e feto.
Il dataset disponibile descrive i dati delle cartelle cliniche delle pazienti gravide e se hanno avuto una insorgenza della placenta previa.

## IL DATASET E' IN FORMATO JSON E CONTIENE LE SEGUENTI COLONNE:

1. Età
2. NumeroGravidanzePregresse
3. NumeroTagliCesareiPregressi
4. PrecedentePlacentaPrevia (0 o 1)
5. SanguinamentiNelSecondoTrimestre (0 o 1)
6. InsulinaSiericaDueOre (microunità per millilitro di sangue)
7. IndiceDiMassaCorporea (peso in chilogrammi diviso l'altezza al quadrato espressa in metri)
8. FecondazioneAssisitita (0 o 1)
9. PazienteAffettaDaPlacentaPrevia (0 o 1 -> colonna target)


## SEQUENZA

1. Caricare i dati JSON e controllare le presenza di eventuali dati mancanti, outlier o inconsistenze. Sostituire i dati mancanti / anomali.
2. Calcolare le statistiche descrittive (media, mediana, deviazione standard) per le variabili.
3. Analizzare correlazioni per trovare le variabili più associate alla placenta previa.
4. Codificare eventuali variabili categoriali e Normalizzre / Standardizzare variabili numeriche.
5. Suddividere i dati in train/test (80%/20%) 
6. Scegliere un algoritmo di classificazione ed eseguire una ricerca dei parametri migliori.
7. Valutare il modello finale e creare una funzione PredictPlacentaPrevia(...) che prende in input le variabili e restituisce le previsione (0 o 1) e la probabilità.
8. Implementare una WebAPI con endpoint/predict che accetta una richiesta POST con i dati della paziente in JSON (raw json), richiama al funzione PredictPlacentaPrevia(...) e restituisce i dati in JSON.
9. Creare una Pagina web (HTML + JavaScript) per inserire i dati della paziente. Inserire un button per inviare i dati all'endpoint Flask via chiamata AJAX/fetch API. Visualizzare la previsione (probabilità di placenta previa) nella pagina.