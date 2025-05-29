# import pandas as pd
# from etl.2_cleaning.1_handle_missing import handle_missing_values
# from etl.2_cleaning.2_remove_duplicates import remove_duplicate_rows
# from etl.2_cleaning.3_filter_outliers import filter_numeric_outliers
# from etl.2_cleaning.4_create_features import create_derived_features

# # Cargar datos
# df = pd.read_csv("../data/student_data.csv")

# # Aplicar limpieza
# df = handle_missing_values(df)
# df = remove_duplicate_rows(df)
# df = filter_numeric_outliers(df)
# df = create_derived_features(df)

# # Guardar resultado
# df.to_csv("../processed/cleaned_data.csv", index=False)