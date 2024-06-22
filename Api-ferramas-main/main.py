from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import pandas as pd
import json

app = FastAPI(title="API Ferremas")

templates = Jinja2Templates(directory="templates")

# Proveedores
df_prov = pd.read_csv("prov.csv")
datos_prov = df_prov["empresa"].to_dict()

@app.get("/")
async def get_proveedores(request: Request):
    sin_codificar = json.dumps(datos_prov)
    json_datos = json.loads(sin_codificar)
    return templates.TemplateResponse("index.html", {"request": request, "listado": json_datos})

@app.post("/agregar")
async def agregar_proveedor(request: Request, new_proveedor: str = Form(...)):
    nuevos_datos = {}
    i = 1
    for id in datos_prov:
        nuevos_datos[id] = datos_prov[id]
        i += 1
    datos_prov[str(i)] = new_proveedor
    df_prov.loc[len(df_prov)] = [i, new_proveedor]
    df_prov.to_csv("prov.csv", index=False)
    return RedirectResponse("/", 303)

@app.get("/eliminar/{id}")
async def eliminar_proveedor(request: Request, id: int):
    del datos_prov[str(id)]
    df_prov.drop(df_prov[df_prov['position'] == id].index, inplace=True)
    df_prov.to_csv("prov.csv", index=False)
    return RedirectResponse("/", 303)

# Productos
productos = [
    {"id": 1, "nombre": "Taladro", "precio": 100.0},
    {"id": 2, "nombre": "Martillo", "precio": 50.0},
]

@app.get("/productos")
async def get_productos(request: Request):
    return templates.TemplateResponse("productos.html", {"request": request, "productos": productos})

@app.post("/productos/agregar")
async def agregar_producto(request: Request, nombre: str = Form(...), precio: float = Form(...)):
    nuevo_producto = {"id": len(productos) + 1, "nombre": nombre, "precio": precio}
    productos.append(nuevo_producto)
    return RedirectResponse("/productos", 303)

@app.get("/productos/eliminar/{id}")
async def eliminar_producto(request: Request, id: int):
    global productos
    productos = [producto for producto in productos if producto["id"] != id]
    return RedirectResponse("/productos", 303)

# Usuarios
usuarios = [
    {"id": 1, "nombre": "Juan Perez"},
    {"id": 2, "nombre": "Maria Gomez"},
]

@app.get("/usuarios")
async def get_usuarios(request: Request):
    return templates.TemplateResponse("usuarios.html", {"request": request, "usuarios": usuarios})

@app.post("/usuarios/agregar")
async def agregar_usuario(request: Request, nombre: str = Form(...)):
    nuevo_usuario = {"id": len(usuarios) + 1, "nombre": nombre}
    usuarios.append(nuevo_usuario)
    return RedirectResponse("/usuarios", 303)

@app.get("/usuarios/eliminar/{id}")
async def eliminar_usuario(request: Request, id: int):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario["id"] != id]
    return RedirectResponse("/usuarios", 303)
