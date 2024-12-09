import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

# Função para construir a rede neural
def build_model(input_shape):
    model = Sequential([
        LSTM(64, activation='relu', input_shape=input_shape, return_sequences=True),
        LSTM(64, activation='relu'),
        Dense(1)  
    ])
    
    model.compile(optimizer='adam', loss='mse')
    
    return model

# Função para treinar a rede neural
def train_model(model, X, y, epochs=10, batch_size=32):
    model.fit(X, y, epochs=epochs, batch_size=batch_size)

# Função para avaliar o modelo
def evaluate_model(model, X_test, y_test):
    loss = model.evaluate(X_test, y_test)
    return loss
