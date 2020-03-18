# Estructura de ficheros
```
├── LICENSE
├── README.md     
├── 01_docs               <- Doc del proyecto
|     
├── 02_data
│   ├── 04_external       <- Datos de terceros
│   ├── 03_processed      <- el dato final procesado con el que se modeliza
│   ├── 02_intermediate   <- Datos intermedios transformados
│   └── 01_raw            <- Datos raw
│
├── 03_research          <- Jupyter notebooks. Nombrados según metodología CRISP-DM.
|   ├── notebooks
|       ├── 01_business_understanding
|       ├── 02_data_understanding
|       ├── 03_data_preparation
|       ├── 04_modeling
|       ├── 05_evaluation
|       ├── 06_deployment
|   ├── scripts
|       ├── src
|       ├── test   
│
├── 04_src                <- Código fuente para el proyecto
|    ├── scala
|    ├── python
|	    ├── venv
|		└── project
|			├── REAME.md
|			├── doc
|			├── bin
|			├── apidoc
|			├── lib
│		    	├── __init__.py    <- para generar la librería
│		    	│
│   			├── data           <- Scripts para descargar y genera datos
│   			│   └── make_dataset.py
│		    	│
│	   		    ├── features       <- Genera a partir de datos raw, datos procesados
│		    	│   └── build_features.py
│			    │
│		    	├── models         
│	    		│   │                 
│		    	│   ├── predict_model.py
│		    	│   └── train_model.py
│	    		│
│		   		├──  visualization  <- scripts para visualización
│		    	│   └── visualize.py
│	    		│
│		   		├──  metrics  <- scripts para métricas de testing
│		    	│   └── metrics.py
│				│
|				└── tox.ini            <- para testing
|
├── 05_models             <- modelos con su output, figuras y métricas
│   └── <model_version> 
|		├── model
|		├── figures
│   	└── predictions
|
├── 06_reports            <- Reports de la modelización		           
│
├── 07_references         <- Diccionario de datos y cualquier material explicativo
│
├── requirements.txt   <- Librerías usadas
│
├── setup.py           <- Para hacer el proyecto instalable
├── config           <- fichero con la configuracion (version,...)
├── MLproject   <- En caso de usar Mlflow
├── conda.yaml   <- En caso de usar conda
├── .git <- fichero de git
├── .gitignore   <- Para no subir todos los datos
├── .env <- fichero con variables no compartibles			
```

## Start

1. Git
	1. git init .
	2. git commit -m "start project"
2. virtualenv
    1.  python3 -m venv ../venv
    2. source activate ../venv
3. .env
	1. env variables

