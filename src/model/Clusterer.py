from sklearn.cluster import KMeans
# from sklearn.metrics import pairwise_distances_argmin_min
from kneed import KneeLocator
import pandas as pd
class Clusterer():

    def __init__(self,data):
        self.data=data
        self.SSE=None
        self.km=None
        self.knee_loc=None
        self.colores=['red','blue','green','yellow',
                        'brown','purple','turquoise','orange',
                        'darkred','deeppink','lime','dimgray']
        self.asignar=[]
        self.centroides=None
        self.num_clusters=4

    def elbow(self):
        data=self.data
        self.SSE=[]
        #Se comprueba de 2 a 12 grupos
        for i in range(2,12):
            km=KMeans(n_clusters=i,random_state=0)
            km.fit(data)
            self.SSE.append(km.inertia_)
        self.knee_loc=KneeLocator(range(2,12),self.SSE,curve='convex',
                                    direction='decreasing').knee
        self.num_clusters=self.knee_loc

    def calcular_clusters(self):
        #Se tiene que paralelizar
        data=self.data
        self.km=KMeans(n_clusters=self.num_clusters,random_state=0).fit(data)
        self.km.predict(data)

    def set_colors(self):
        #Se tiene que paralelizar
        asignar_aux=[]
        for grupo in self.km.labels_:
            asignar_aux.append(self.colores[grupo])
        self.asignar=asignar_aux

    def calcular_centroides(self):
        #Se tiene que paralelizar
        data=self.data
        self.centroides=self.km.cluster_centers_
        self.centroides=pd.DataFrame(self.centroides.round(4),
            columns=data.columns)
        self.centroides['Color']=self.colores[0:self.num_clusters]
