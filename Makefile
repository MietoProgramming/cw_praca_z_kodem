setup:
	pip install -r requirements.txt
lint:
	pylint app.py --disable=missing-docstring
run: setup lint
	flask run