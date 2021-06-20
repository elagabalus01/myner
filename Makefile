rebuild:build build_res run

run:
	echo "Corriendo el programa"
	python -B app.py

test: build
	echo "Realizando las pruebas"
	python -B test.py

build: ./views/Ui_MainWindow.py ./views/FS/Ui_FeatureSelectionWidget.py ./views/FS/Ui_VisualEvaluation.py ./views/FS/Ui_Correlation.py
	echo "Actualizando la interfaz"

build_res: ./res_rc.py
	echo "Actualizando paquete de recursos"

./res_rc.py: ./res/res.qrc
	pyrcc5 -o ./res_rc.py ./res/res.qrc

./views/Ui_MainWindow.py: ./ui_src/interfaz.ui
	pyuic5 ./ui_src/interfaz.ui -o ./views/Ui_MainWindow.py

./views/FS/Ui_FeatureSelectionWidget.py: ./ui_src/FS/FeatureSelectionWidget.ui
	pyuic5 ./ui_src/FS/FeatureSelectionWidget.ui -o ./views/FS/Ui_FeatureSelectionWidget.py

./views/FS/Ui_VisualEvaluation.py: ./ui_src/FS/VisualEvaluation.ui
	pyuic5 ./ui_src/FS/VisualEvaluation.ui -o ./views/FS/Ui_VisualEvaluation.py

./views/FS/Ui_Correlation.py: ./ui_src/FS/Correlation.ui
	pyuic5 ./ui_src/FS/Correlation.ui -o ./views/FS/Ui_Correlation.py

.SILENT: run test build
