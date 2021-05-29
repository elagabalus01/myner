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
