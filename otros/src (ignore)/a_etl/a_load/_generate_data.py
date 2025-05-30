# Genera datos ficticios (si no hay fuente real)

# import pandas as pd
# import numpy as np

# np.random.seed(42)
# df = pd.DataFrame({
#     "edad": np.random.randint(17, 25, 100),
#     "promedio": np.round(np.random.uniform(2.0, 5.0, 100), 2),
#     "asistencia": np.random.randint(50, 100, 100),
#     "actividad_extra": np.random.choice([0, 1], 100),
#     "horas_estudio": np.random.randint(1, 10, 100),
#     "desercion": np.random.choice([0, 1], 100, p=[0.8, 0.2])
# })

# os.makedirs("data", exist_ok=True)
# df.to_csv("data/student_data.csv", index=False)
# print("Datos generados")