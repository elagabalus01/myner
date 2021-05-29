from controller.analisis_exploratorio.preview_table import PreviewTableController
from model.load_csv import datos
def print_detail(objeto):
    print(objeto,type(objeto),sep=",")
sub_dataframe=datos.head(10)
print_detail(sub_dataframe)

def data_preview(datos,n_rows):
    for i in range(len(datos.columns)):
        column_name=str(datos.columns[i])
        print(column_name)
        for j in range(n_rows):
            print(datos[column_name][j])
