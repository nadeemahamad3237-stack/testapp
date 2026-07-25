`
```python
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

class AIModel:
    def __init__(self):
        self.model = None

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        self.model = keras.Sequential([
            keras.layers.Dense(64, activation='relu', input_shape=(X.shape[1],)),
            keras.layers.Dense(32, activation='relu'),
            keras.layers.Dense(len(set(y)))
        ])
        self.model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        self.model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

    def predict(self, X):
        return self.model.predict(X)
```

#