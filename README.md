# Poblar-Ar Análisis Demográfico de la República Argentina 
<div align="center">

<img src="./Logotipo poblar-AR con bandera argentina.png" alt="Logo Poblar-AR" width="500">
</div>

## **Descripción del proyecto**

El proyecto consiste en el desarrollo de una **aplicación de consola utilizando Python**, orientada al **análisis y la visualización de datos demográficos de la República Argentina**.
Al iniciar la aplicación, el usuario podrá interactuar con un **menú de opciones** que le permitirá consultar, filtrar y analizar información demográfica mediante diferentes criterios, como **provincias, localidades, cantidad de habitantes y tipos de viviendas**, entre otros parámetros.
Además, la aplicación contará con herramientas de **visualización de datos mediante gráficos**, que permitirán interpretar y comparar la información de manera más sencilla. Los gráficos generados podrán **exportarse en formato PNG** para su posterior consulta, presentación o utilización en otros informes.

## **Creación y origen de la base de datos**

La base de datos utilizada en el proyecto fue construida a partir de información oficial del **Censo Nacional de Población, Hogares y Viviendas 2022**, realizado por el Instituto Nacional de Estadística y Censos (INDEC) de la República Argentina.

### **Fuente de datos oficial**

Los datos primarios fueron obtenidos a través de la plataforma de consulta en línea **Redatam**, proporcionada por el INDEC, que permite acceder y procesar la información censal mediante diferentes criterios de selección y filtrado.

**Plataforma de extracción:** [INDEC - Redatam | Censo 2022](https://redatam.indec.gob.ar/binarg/RpWebEngine.exe/Portal?BASE=CPV2022&lang=ESP)

### **Proceso de extracción y construcción**

Para conformar la base de datos del proyecto, se realizaron diferentes consultas y filtros sobre los datos censales disponibles en Redatam, seleccionando la información necesaria para el análisis demográfico.
Posteriormente, los datos obtenidos fueron organizados y estructurados en formato csv para facilitar su procesamiento mediante Python y permitir la realización de consultas, análisis estadísticos y visualizaciones.

### **Organismo responsable**

- **Institución:** Instituto Nacional de Estadística y Censos (INDEC).
- **Fuente:** Censo Nacional de Población, Hogares y Viviendas 2022.
- **Herramienta de extracción:** Redatam.
- **Cobertura geográfica:** República Argentina.

## Instalación

Requiere Python 3.10 o superior.

```bash
git clone https://github.com/Aghuz2021/Poblar_ar.git
cd Poblar-Ar

python -m venv .venv
# Windows (PowerShell):  .venv\Scripts\Activate.ps1
# Mac/Linux:             source .venv/bin/activate

pip install -r requirements.txt
```

## **Estructura del proyecto**
```text
Poblar-Ar/
│
├── Conexion/          # Módulos encargados de la conexión y carga segura de datos
├── Data/              # Archivos de datos y fuentes CSV 
├── Filtros/           # Funciones y lógica para el filtrado y procesamiento de datos
├── notebooks/         # Jupyter Notebooks para análisis exploratorio y pruebas
├── .gitattributes     # Configuración de control de versiones Git
├── .gitignore         # Archivos y directorios ignorados por Git
├── requirements.txt   # Dependencias y librerías necesarias de Python
├── Logotipo poblar-AR con bandera argentina.png  # Imagen del logotipo oficial
└── README.md          # Documentación principal del repositorio
```
