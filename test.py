from model.load_csv import datos
def print_detail(objeto):
    print(objeto,type(objeto),sep=",")

# sub_dataframe=datos.head(10)
# print_detail(sub_dataframe)

def data_preview(datos,n_rows):
    for i in range(len(datos.columns)):
        column_name=str(datos.columns[i])
        print(column_name)
        for j in range(n_rows):
            print(datos[column_name][j])

def data_missed(datos):
    missed=datos.isnull().sum()
    cols=datos.axes[1]
    # print_detail(missed)
    for i in range(len(missed)):
        print_detail(cols[i])
        print_detail(missed[i])

def test_graphics():
    # import matplotlib.pyplot as plt
    print(datos.plot().plot([0,1,2,3,4], [10,1,20,3,40]))
# test_graphics()
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

print(matplotlib.pyplot)
figure=plt.figure()
ax=figure.add_subplot(2,2,1)
bx=figure.add_subplot(2,2,2)
ax.plot([1,2,3,4,5])
bx.plot([3,2,1,0,-1])
print_detail(ax.__dict__)
print_detail(ax.figure)
datos.hist(figsize=(12,12),xrot=45)
print_detail(datos.plot())
plt.show()
# figure.close()
