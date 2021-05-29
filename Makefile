run:
	echo "Corriendo el programa"
	python -B app.py

test:
	echo "Realizando las pruebas"
	python -B test.py

build: ./views/main_view.py
	echo "Actualizando la interfaz"

./views/main_view.py: ./views/interfaz.ui
	pyuic5 ./views/interfaz.ui -o ./views/main_view.py

.SILENT: run test build
