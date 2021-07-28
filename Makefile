views=./src/views
src=./ui_src
res=./src/res
fs_view=$(views)/FS
eda_view=$(views)/EDA
fs_src=$(src)/FS
eda_src=$(src)/EDA
km_view=$(views)/Kmeans
km_src=$(src)/kmeans
ar_src=$(src)/Asociacion
ar_view=$(views)/Asociacion
my_res_src=$(src)/res/res.qrc
breeze_res_src=$(src)/QBreeze/qbreeze.qrc

resources=$(res)/res_rc.py\
			$(res)/breeze_rc.py

app_views=$(views)/Ui_LoadingScreen.py\
		$(views)/Ui_MainWindow.py

eda_views=$(eda_view)/Ui_EDA_Widget.py

fs_views=$(fs_view)/Ui_FeatureSelectionWidget.py\
		$(fs_view)/Ui_VisualEvaluation.py\
		$(fs_view)/Ui_Correlation.py\
		$(fs_view)/Ui_PCA.py

km_views=$(km_view)/Ui_ElbowWidget.py\
		$(km_view)/Ui_KmeansWidget.py\
		$(km_view)/Ui_ClustersWidget.py

ar_views=$(ar_view)/Ui_AprioriWidget.py


rebuild:build build_res run

run:
	echo "Corriendo el programa"
	python -B ./src/app.py

test: build
	echo "Realizando las pruebas"
	python -B ./src/test.py

build:$(app_views)  $(fs_views) ${eda_views} ${km_views} $(ar_views) ${resources}
	echo "Actualizando la interfaz"

build_res: $(resources)
	echo "Actualizando paquete de recursos"

$(res)/res_rc.py: $(my_res_src)
	pyrcc5 $< -o $@
$(res)/breeze_rc.py: $(breeze_res_src)
	pyrcc5 $< -o $@

$(views)/Ui_MainWindow.py: $(src)/MainWindow.ui
	pyuic5 $< -o $@ --import-from=res

$(views)/Ui_LoadingScreen.py: $(src)/loading_screen.ui
	pyuic5 $< -o $@

$(fs_view)/Ui_FeatureSelectionWidget.py: $(fs_src)/FeatureSelectionWidget.ui
	pyuic5 $< -o $@

$(fs_view)/Ui_VisualEvaluation.py: $(fs_src)/VisualEvaluation.ui
	pyuic5 $< -o $@

$(fs_view)/Ui_Correlation.py: $(fs_src)/Correlation.ui
	pyuic5 $< -o $@

$(fs_view)/Ui_PCA.py: $(fs_src)/Componentes.ui
	pyuic5 $< -o $@

$(eda_view)/Ui_EDA_Widget.py: $(eda_src)/eda.ui
	pyuic5 $< -o $@

$(km_view)/Ui_ElbowWidget.py: $(km_src)/Elbow.ui
	pyuic5 $< -o $@ --import-from=res

$(km_view)/Ui_KmeansWidget.py:$(km_src)/kmeans.ui
	pyuic5 $< -o $@

$(km_view)/Ui_ClustersWidget.py:$(km_src)/clusters.ui
	pyuic5 $< -o $@ --import-from=res

$(ar_view)/Ui_AprioriWidget.py:$(ar_src)/apriori.ui
	pyuic5 $< -o $@

.SILENT: run test build
