# Bitácora de Desarrollo — RequestFlow API

Proyecto: **Proyecto 001 — RequestFlow API**  
Tipo: Backend API REST  
Stack principal: Python, FastAPI, PostgreSQL, SQLAlchemy, Alembic, Pydantic, JWT, RBAC, Docker, Pytest.  
Objetivo: construir una API backend profesional para la gestión de solicitudes institucionales o empresariales, con autenticación, roles, permisos, trazabilidad y documentación técnica.

---

## Estado general del proyecto

El proyecto se encuentra en fase de construcción del backend base.  
Ya cuenta con estructura profesional, control de versiones con Git/GitHub, configuración inicial, conexión preparada a PostgreSQL, migraciones con Alembic, modelo de usuarios, schemas Pydantic, cifrado de contraseñas, repositorio de usuarios y endpoint inicial para creación de usuarios desde Swagger.

---

## Bloques ejecutados

### Bloque 1 — Inicialización del proyecto

Se creó la carpeta local del proyecto en:

`C:\Proyectos Backend\001_RequestFlow_API`

Se inicializó Git y se crearon los archivos base:

- `README.md`
- `.gitignore`

Resultado verificable:

- Repositorio Git inicializado.
- Primer commit realizado.
- Proyecto conectado posteriormente con GitHub.

Commits relacionados:

- `chore: initialize RequestFlow API project`
- `docs: add initial project documentation and gitignore rules`

---

### Bloque 2 — Conexión con GitHub

Se creó el repositorio remoto en GitHub y se conectó con el repositorio local mediante `origin`.

Resultado verificable:

- Proyecto local conectado con GitHub.
- Rama principal configurada como `main`.
- Primer push realizado correctamente.

---

### Bloque 3 — Estructura base del backend

Se creó la estructura inicial del proyecto FastAPI:

```text
app/
├── api/
├── core/
├── db/
├── models/
├── repositories/
├── schemas/
├── services/
├── tests/
└── main.py
```

### Bloque 4 — Entorno virtual y dependencias iniciales

Se creó el entorno virtual venv y se instalaron dependencias iniciales:

FastAPI
Uvicorn

Se generó el archivo:

requirements.txt

Resultado verificable:

Entorno virtual activo.
FastAPI instalado.
Dependencias registradas.

Commit relacionado:

chore: add initial FastAPI dependencies

### Bloque 5 — API mínima

Se creó la primera API mínima con FastAPI.

Endpoints iniciales:

GET /
GET /health

Resultado verificable:

API ejecutándose en http://127.0.0.1:8000
Swagger disponible en http://127.0.0.1:8000/docs
OpenAPI disponible en /openapi.json

Commit relacionado:

feat: add minimal FastAPI application

### Bloque 6 — Configuración base del proyecto

Se agregó configuración centralizada mediante pydantic-settings.

Archivos trabajados:

app/core/config.py
.env.example
app/main.py

Variables configuradas:

PROJECT_NAME
PROJECT_VERSION
PROJECT_DESCRIPTION
ENVIRONMENT

Resultado verificable:

La API responde mostrando el ambiente development.
La configuración ya no está quemada directamente en main.py.

Commit relacionado:

chore: add application settings configuration

### Bloque 7 — Separación de rutas Health

Se separaron las rutas principales del archivo main.py.

Archivos trabajados:

app/api/health.py
app/main.py

Endpoints mantenidos:

GET /
GET /health

Resultado verificable:

Las rutas siguen funcionando.
main.py queda más limpio y organizado.

Commit relacionado:

refactor: separate health routes from main application

### Bloque 8 — Configuración de base de datos

Se agregó la variable DATABASE_URL en la configuración del proyecto.

Archivos trabajados:

.env.example
app/core/config.py

Configuración local:

postgresql+psycopg://postgres:postgres@localhost:5432/requestflow_db

Resultado verificable:

El proyecto queda preparado para conectarse a PostgreSQL.

Commit relacionado:

chore: add database configuration settings

### Bloque 9 — Dependencias de base de datos

Se instalaron dependencias para base de datos y migraciones:

SQLAlchemy
Alembic
psycopg

Archivo actualizado:

requirements.txt

Resultado verificable:

Dependencias instaladas en el entorno virtual.
Dependencias registradas en requirements.txt.

Commit relacionado:

chore: add database dependencies

### Bloque 10 — Configuración SQLAlchemy

Se creó la configuración inicial de SQLAlchemy.

Archivos trabajados:

app/db/session.py
app/db/database.py

Componentes creados:

engine
SessionLocal
Base
get_db

Resultado verificable:

El proyecto cuenta con motor de conexión, sesión de base de datos y dependencia para FastAPI.

Commits relacionados:

chore: add SQLAlchemy session configuration
chore: add database session dependency

### Bloque 11 — Inicialización de Alembic

Se inicializó Alembic para manejar migraciones.

Archivos y carpetas creadas:

alembic/
alembic.ini

Se configuró alembic/env.py para usar:

settings.DATABASE_URL
Base.metadata
importación de modelos

Resultado verificable:

Alembic inicializado.
Configurado para leer la URL de base de datos desde la configuración del proyecto.

Commit relacionado:

chore: initialize Alembic migrations

### Bloque 12 — Modelo User

Se creó el primer modelo SQLAlchemy del proyecto.

Archivo creado:

app/models/user.py

Tabla definida:

users

Campos principales:

id
full_name
email
hashed_password
role
is_active
created_at
updated_at

Resultado verificable:

Modelo User creado y registrado para Alembic.

Commit relacionado:

feat: add user model

### Bloque 13 — Migración de tabla users

Se generó la primera migración con Alembic.

Comando usado:

alembic revision --autogenerate -m "create users table"

Luego se aplicó la migración:

alembic upgrade head

Resultado verificable en pgAdmin:

Tabla users creada.
Tabla alembic_version creada.

Commit relacionado:

feat: add users table migration

### Bloque 14 — Schemas Pydantic de usuario

Se crearon los schemas para entrada y salida de usuarios.

Archivo creado:

app/schemas/user.py

Schemas definidos:

UserBase
UserCreate
UserUpdate
UserResponse

Dependencia agregada:

email-validator

Resultado verificable:

Schemas creados.
Validación de email habilitada.
Respuesta de usuario preparada para no exponer contraseña.

Commit relacionado:

feat: add user schemas

### Bloque 15 — Seguridad de contraseñas

Se agregó cifrado y verificación de contraseñas.

Archivo creado:

app/core/security.py

Funciones creadas:

get_password_hash
verify_password

Dependencias usadas:

Passlib
bcrypt

Ajuste técnico:

Se fijó bcrypt==4.0.1 para evitar incompatibilidad con Passlib.

Resultado verificable:

Hash generado correctamente.
Contraseña correcta devuelve True.
Contraseña incorrecta devuelve False.

Commit relacionado:

feat: add password hashing utilities

### Bloque 16 — Repositorio de usuarios

Se creó la capa de acceso a datos para usuarios.

Archivo creado:

app/repositories/user_repository.py

Funciones creadas:

get_user_by_email
get_user_by_id
create_user

Resultado verificable:

Usuario administrador creado desde consola Python.
Contraseña guardada como hash bcrypt.
Fila verificada en pgAdmin dentro de public.users.

Commit relacionado:

feat: add user repository

### Bloque 17 — Endpoint de creación de usuarios

Se creó el primer endpoint funcional de usuarios.

Archivo creado:

app/api/users.py

Archivo modificado:

app/main.py
app/db/database.py

Endpoint creado:

POST /users/

Funcionalidad:

Recibe datos mediante UserCreate.
Valida si el correo ya existe.
Crea usuario con contraseña cifrada.
Devuelve UserResponse.
No expone password ni hashed_password.

Resultado verificable:

Endpoint visible en Swagger.
Usuario creado desde POST /users/.
Respuesta 201 Created.
Respuesta sin contraseña ni hash.

Commit relacionado:

feat: add user creation endpoint

### Observaciones técnicas importantes

El backend es el núcleo principal del proyecto.
La vitrina visual mínima se implementará más adelante, cuando existan login, JWT, solicitudes y métricas básicas.
No se usará React en esta fase inicial.
La vitrina recomendada será simple: FastAPI + HTML + CSS + JavaScript básico consumiendo la API.
El proyecto debe mantenerse documentado para GitHub, entrevistas y portafolio profesional.