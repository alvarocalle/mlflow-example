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
2. ipython notebook 

