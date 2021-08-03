from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import numpy as np

class Classifier():
    def __init__(self,model):
        self.model=model
        self.regression = LogisticRegression()
        self.test_percentage=None
        self.dependiente=None
        self.vector_entrada=None
        self.encoder=None
        self.decoder=lambda x:list(self.encoder.keys())[list(self.encoder.values()).index(x)]

    def generar_modelo(self):
        if self.model and self.dependiente and self.test_percentage:
            dependiente=self.dependiente
            data=self.model.clean_numeric_data
            all_data=self.model.clean_data
            test_percentage=self.test_percentage
            if dependiente in data.columns:
                X=data.drop([dependiente],axis=1)
            else:
                X=data
            print(X.shape)
            X=np.array(X)

            unique_values=all_data[dependiente].unique()
            encoder={}
            i=0
            for value in unique_values:
                encoder[value]=i
                i+=1
            all_data=all_data.dropna()
            Y=all_data[dependiente]
            print(Y.shape)
            Y=np.array(Y.replace(encoder))
            seed=1234
            X_train, X_validation, Y_train, Y_validation = train_test_split(
                X, Y, test_size=test_percentage,
                random_state=seed, shuffle = True
            )
            self.regression.fit(X_train, Y_train)
            self.encoder=encoder
        else:
            raise Exception("No se configuraron los datos para generar el modelo")

    def calcular_prediccion(self):
        vector_entrada=self.vector_entrada
        if vector_entrada:
            np.array(vector_entrada)
            result = self.regression.predict([vector_entrada])
            self.vector_entrada=None
            return str(self.decoder(result[0]))
        else:
            raise Exception("Error: No se encontró el vector de entrada")
