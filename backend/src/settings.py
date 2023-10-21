import os

from dotenv import load_dotenv
from tinydb import TinyDB
from tinydb.storages import JSONStorage
from tinydb_serialization import SerializationMiddleware
from tinydb_serialization.serializers import DateTimeSerializer

from LSB_recognizer_model.src.coordenates.models.coordenates_models import (
    INPUT_SHAPE_FIX,
    get_model_coord_dense_3,
)

# ----------------- Environment Variables ----------------- #

load_dotenv()
PYTHONUNBUFFERED = os.getenv("PYTHONUNBUFFERED")
SECRET = os.getenv("SECRET")

# ----------------- PATHS --------------------------

PATH_PREDICTED_IMG = os.getenv("PATH_PREDICTED_IMG")

PATH_RAW_SIGNS = os.getenv("PATH_RAW_SIGNS")
PATH_NUMPY_COORDS = os.getenv("PATH_NUMPY_COORDS")

PATH_MODELS = os.getenv("PATH_MODELS")
PATH_DB = os.getenv("PATH_DB")

# ----------------- Database variables --------------------------

serialization = SerializationMiddleware(JSONStorage)
serialization.register_serializer(DateTimeSerializer(), "TinyDate")

# Asegúrate de que la ruta a la base de datos es correcta y que el archivo db.json existe
db_path = os.path.join(os.path.dirname(__file__), PATH_DB, "db.json") 
#db_path = os.path.join(os.getcwd(), PATH_DB, "db.json")
if not os.path.exists(db_path):
    raise FileNotFoundError(f"No se pudo encontrar el archivo de base de datos: {db_path}")

tinydb = TinyDB(db_path, storage=serialization)
signal_table = tinydb.table("signals")
users_table = tinydb.table("users")
models_table = tinydb.table("models")

# ----------------- Model variables --------------------------

neuronal_network = get_model_coord_dense_3
INPUT = INPUT_SHAPE_FIX

