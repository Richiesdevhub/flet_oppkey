
#Comando para bajar el packete de uv para python
curl -LsSf https://astral.sh/uv/install.sh | sh

#Iniciar un proyecto con uv(descripcion en su página tambien):
uv init --python=3.13 <nombre_proyecto> #Opcion de instalar python 3.13

#Crear el venv, lo inicia, instala flet y actualiza dependencias con toml
uv add "flet[all]"

#Comando para iniciar el venv
>.venv\Scripts\activate
