import os
import pandas as pd
from functools import wraps

def backup_before(group_name):
    """
    Decorador para hacer backup antes de ejecutar una tarea del grupo
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Ruta base
            input_path = kwargs.get("input_path", "..data/processed/current_state.csv")
            output_dir = "../data/processed/backups"
            filename = f"{group_name}_before_{func.__name__}.csv"

            # Cargar datos
            df = pd.read_csv(input_path)

            # Guardar backup
            os.makedirs(output_dir, exist_ok=True)
            full_path = os.path.join(output_dir, filename)
            df.to_csv(full_path, index=False)
            print(f"Backup realizado antes de {func.__name__} → {full_path}")

            # Ejecutar la función original
            return func(*args, **kwargs)
        return wrapper
    return decorator