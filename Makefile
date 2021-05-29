run:
	echo "Corriendo el programa"
	python -B app.py
	
test:
	echo "Realizando las pruebas"
	python -B test.py

.SILENT: run test
