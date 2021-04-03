build:
	docker build --no-cache -t flask-math-solver .

run:
	docker run --rm -p 5000:5000 flask-math-solver:latest

test:
	pytest . --disable-warnings
