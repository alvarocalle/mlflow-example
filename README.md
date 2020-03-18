# Estructura de ficheros
Ejemplo de funcionamiento de MLflow
```
├── 03_research          <- Jupyter notebooks. Nombrados según metodología CRISP-DM.
|   ├── notebooks
|       ├── 04_modeling
├── 04_src                <- Código fuente para el proyecto
|    ├── python
|	└── project
|		├── REAME.md
|		├── doc
|		├── bin
|		├── apidoc
|		├── lib
│	    	├── __init__.py    <- para generar la librería
│	    	│
│  		├── data           <- Scripts para descargar y genera datos
│  		│   └── make_dataset.py
│	    	│
│	   	├── features       <- Genera a partir de datos raw, datos procesados
│		│   └── build_features.py
│	        │
│		├── models         
│	    	│   │                 
│		│   ├── predict_model.py
│		├──  metrics  <- scripts para métricas de testing
│		│   └── metrics.py
|
├── 05_models             <- modelos con su output, figuras y métricas
│   └── <model_version> 
|		├── model
|		├── figures
│   	└── predictions
|
│
├── MLproject   <- En caso de usar Mlflow
├── conda.yaml   <- En caso de usar conda
├── .git <- fichero de git
├── .gitignore   <- Para no subir todos los datos
├── .env <- fichero con variables no compartibles			
```

## Start
1. conda env create -f environment.yml
2. conda source env
3. source .env 
4. mlflow run .
5. mlflow models serve -m models/mlruns/0/0ab9ada381604109b569b52fe0655431/artifacts/model -p 1234
6. curl -X POST -H "Content-Type:application/json" --data '[{"fixed acidity": 6.2, "volatile acidity": 0.66, "citric acid": 0.48, "residual sugar": 1.2, "chlorides": 0.029, "free sulfur dioxide": 29, "total sulfur dioxide": 75, "density": 0.98, "pH": 3.33, "sulphates": 0.39, "alcohol": 12.8}]' http://127.0.0.1:1234/invocations


