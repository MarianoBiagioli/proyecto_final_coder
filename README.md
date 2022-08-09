# Proyecto final de Coder

Proyecto final de Martin Grosvald y Mariano Biagioli. 

El proyecto consiste en una web para publicar clases particulares.

Este proyecto tiene por objetivo que docentes puedan registrarse y publicar sus clases de apoyo y que los posibles alumnos puedan acceder a ellos y contactarse a través de los datos que los docentes publiquen.

Los usuarios/docentes pueden:

- Crear y modificar su usuario.
- Crear, modificar y eliminar sus Avisos.
- Los avisos quedarán visibles desde la página index/principal.
- Se podrán buscar los avisos desde la misma pagina index/principal.

Para ver video y casos de prueba, ingresar en el siguiente link: https://drive.google.com/drive/folders/1eGIbq_bE5jgghS0KGlGZoHSRxs-JkCMb?usp=sharing

# Instalar 

Para instalar este sitio, se necesitará:

## Python
Este proyecto se escribió en python 3.8.0. 

Cómo reviso mi versión de python?

en *nix systems:

```bash
> python --version
> Python 3.8.0
```

en windows:

```bash
c:\> py --version
c:\> Python 3.8.0
```

## Instalación de Dependencias

Para instalar las dependencias, necesitas correr `pip install`. Asegurarse de estar en la carpeta del proyecto y que puedas ver el archivo `requirements.txt` cuando hagas `ls` o `dir`:

```bash
> pip install -r requirements.txt
```

`Algunos sistemas operativos podrán requerir el uso de pip3 en lugar de pip `

## Configurar las aplicaciones de Django

Una vez finalizada la instalación de las dependencias, necesitaras instalar algunos comandos de Django.

### Migrations

Iniciar la base de datos.

*nix:
```bash
> python mananage.py migrate
```
windows:
```bash
c:\> py mananage.py migrate
```

### Correr el servidor.

```bash
> python mananage.py runserver
```
windows:
```bash
c:\> py mananage.py runserver
```