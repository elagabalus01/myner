from apyori import apriori
class AprioriController():
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.bind_signals()

    def bind_signals(self):
        pass
        # self.view.btn_gen_rules.clicked.connect(self.calcular)

    def set_model(self):
        self.calcular()
        # self.view.feature1_box.clear()
        # self.view.feature2_box.clear()
        # for feature in self.model.numeric_columns():
        #     self.view.feature1_box.addItem(feature)
        #     self.view.feature2_box.addItem(feature)

    def calcular(self):
        lista_datos = []
        data=self.model.data
        for i in range(1, data.shape[0]): #Para cada transacción
            lista_datos.append([
                data.values[i,j] for j in range(0, data.shape[1])
            ])
        reglas = apriori(lista_datos, min_support=0.01, min_confidence=0.1, min_lift=1)
        reglas_asociacion = list(reglas)
        clean_rules=[]
        for regla in reglas_asociacion:
            items=[item for item in regla.items]
            if 'nan' not in items:
                stats=regla.ordered_statistics[0]
                print("{0}, Support {1:.2f} confidence {2:.2f}, lift {3:.2f}".format(
                    items,regla.support,stats.confidence,stats.lift)
                )
                clean_rules.append(regla)
        len(clean_rules)
