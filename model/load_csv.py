import pandas as pd

def getDataFrame(filepath):
    return pd.read_csv(filepath)

datos=pd.read_csv('data.csv')
renglones=datos.axes[0]
header=datos.axes[1]
# for i in range(0,len(header)):
#     print(header[i],type(header[i]),sep='')
# for column in header:
#     print(column,type(column),sep=',')
def get_head_dtype(data):
    cols=datos.axes[1]
    n_col=len(cols)
    for i in range(0,n_col):
        print(cols[i],data[cols[i]].dtype)
