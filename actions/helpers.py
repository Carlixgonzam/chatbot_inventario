import joblib

def cargar_modelo_prediccion():
    return joblib.load('models_ml/predict_demand_model.pkl')

def predecir_demanda(producto, mes):
    modelo = cargar_modelo_prediccion()
    # Aquí se incluirían los datos relevantes para la predicción
    # Ejemplo de predicción:
    prediccion = modelo.predict([[mes]])
    return prediccion[0]
