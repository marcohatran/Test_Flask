# Test_Flask
## How to run:
### Run with docker:
- Build images ```docker build --tag flask-service:v1 .```
- Run container ```docker run -p 5000:5000 flask-service:v1```
### Run without docker:
- Create environment ```python3 -m venv venv```
- Activate ```source venv/bin/activate```
- Install lib and package ```pip install -r requirements.txt```
- Run server ```python -m flask run```

### How to use:
```curl --location --request POST 'http://0.0.0.0:5000/distance' --form 'address="{address}"'```
### Unittest:
- ```python app_unittest.py```
