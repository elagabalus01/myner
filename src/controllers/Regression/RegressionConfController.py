from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import numpy as np
class RegressionConfController:
    def __init__(self,model,view,clasifier):
        self.model=model
        self.view=view
        self.clasifier=clasifier
        self.bind_signals()

    def bind_signals(self):
        self.view.btn_calcular.pressed.connect(self.generar_modelo)

    def generar_modelo(self):
        test_persentage=self.view.test_percentage.value()/10
        dependiente=self.view.features_box.currentText()
        data=self.model.clean_numeric_data
        all_data=self.model.data
        if dependiente in data.columns:
            X=data.drop([dependiente],axis=1)
        else:
            X=data
        X=np.array(X)

        unique_values=all_data[dependiente].unique()
        encoder={}
        i=0
        for value in unique_values:
            encoder[value]=i
            i+=1
        Y=np.array(all_data[dependiente].replace(encoder))
        print(Y)
        
        # X = np.array(data[['Texture', 'Area', 'Smoothness', 'Compactness', 'Symmetry', 'FractalDimension']])
        # Y = np.array(data[['Diagnosis']]) 
        seed=1234
        X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y,
            test_size=test_persentage,random_state=seed, shuffle = True)
        print(X)
        print(Y_train)
        print(Y_validation)
        self.clasifier.fit(X_train, Y_train)

    def set_model(self):
        self.view.features_box.clear()
        for feature in self.model.objects:
            self.view.features_box.addItem(feature)





