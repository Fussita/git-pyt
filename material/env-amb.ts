
// PIP : Python Package Index 

/*
    Ambientes Virtuales

    Es un directorio autónomo que contiene su propio intérprete y bibliotecas Python, 
    separado de la instalación Python de todo el sistema. 
    
    Crear un espacio aislado donde se pueden instalar paquetes sin afectar al sistema. 
    
    Esto permite evitar conflictos de paquetes entre diferentes proyectos, y también 
    facilita la administración de las dependencias de cada proyecto.

    Beneficios
    Gestión de Dependencias y versiones
    Evitar Contaminación del sistemas y de proyectos
    Portabilidad: Los ambientes virtuales se pueden compartir
    Mantenimiento: al aislar los proyectos

    # CREAR AMBIENTE
    python3 -m venv venv
    
    # EN CMD PROMPT
    venv\Scripts\activate

    # EN POWERSHELL
    .\venv\Scripts\activate.ps1

    # DESACTIVAR EL AMBIENTE VIRTUAL
    deactivate

    # pip install novas
    # Para versiones especificas
    # pip install request==2.6.0

    # pip uninstall
    
    
    # OBTENER INFO DEL PAQUETE
    pip show requests

    # OBTENER LISTA DE DEPENDENCIAS
    pip list
\
    # OBTENER LISTA DE DEPENDENCIAS
    pip freeze > requirements.txt

    SE PUEDE USAR EL ARCHIVO requerements.txt
    pip install -r requirements.txt


*/

/* 
    ALGUNOS PROYECTOS DE PYTHON NO USAN PIP
    SINO QUE USAN POETRY EL CUAL ES UN GESTOR
    DE PAQUETES MODERNOS QUE SIMPLIFICA MUCHO LA
    GESTION DE DEPENDENCIAS

    OFRECE UN ENFORQUE MAS ESTRUCTURADO Y UNIFICADO

    oFRECE UNA GESTION DE DEPENDENCIAS MAS ROBUSTAS, UTILIZA
    UN ARCHIVO pyproject.toml PARA DEFINIR DEPENDENCIAS FACILITANDO
    CONFLICTOS DE VERSIONES Y REPRODUCIBILIDAD
    
    FLUJO DE TRABAJO MAS EFICIENTE, PERMITE CREAR ENTORNOS VIRTUALES
    CON UN COMANDO, INSTALAR Y ACTUALZIAR PAQUETES MUY FACIL, ETC.
    
    MEJOR INTEGRACION CON OTRAS HERRAMIENTAS COMO LINTERS, FORMATEADORES
    Y HERRAMIENTAS DE TESTING

*/

