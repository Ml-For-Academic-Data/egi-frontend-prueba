import pandas as pd
import panel as pn
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

pn.extension('plotly')

# Cargo el dataset
df = pd.read_csv('/data/processed/cleaned_data.csv')


# Columnas categóricas para seleccionar
categorical_columns = [
    'Marital status', 'Application mode', 'Course', 'Gender', 'Target'
]

# Rango de edad
min_age, max_age = df['Age at enrollment'].min(), df['Age at enrollment'].max()

# Widgets
var_select = pn.widgets.Select(name='Variable categórica', options=categorical_columns, value=categorical_columns[0])
age_slider = pn.widgets.IntRangeSlider(name='Rango de edad', start=min_age, end=max_age, value=(min_age, max_age))

@pn.depends(var_select, age_slider)
def plot_histogram(variable, age_range):
    dff = df[(df['Age at enrollment'] >= age_range[0]) & (df['Age at enrollment'] <= age_range[1])]
    fig = px.histogram(dff, x=variable, color='Target', barmode='group', title=f'Histograma de {variable} por Target')
    return fig

@pn.depends(var_select, age_slider)
def plot_boxplot(variable, age_range):
    dff = df[(df['Age at enrollment'] >= age_range[0]) & (df['Age at enrollment'] <= age_range[1])]
    plt.figure(figsize=(8,4))
    sns.boxplot(x=variable, y='Age at enrollment', data=dff)
    plt.title(f'Boxplot de Edad según {variable}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.close()
    return pn.pane.Matplotlib(plt.gcf(), dpi=144)

@pn.depends(age_slider)
def plot_corr_matrix(age_range):
    dff = df[(df['Age at enrollment'] >= age_range[0]) & (df['Age at enrollment'] <= age_range[1])]
    numeric_cols = dff.select_dtypes(include='number').columns
    corr = dff[numeric_cols].corr()
    plt.figure(figsize=(7,7))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
    plt.title('Matriz de Correlación (variables numéricas)')
    plt.tight_layout()
    plt.close()
    return pn.pane.Matplotlib(plt.gcf(), dpi=144)

# Layout
dashboard = pn.Column(
    "# Dashboard Interactivo de Dataset",
    pn.Row(
        pn.Column(var_select, age_slider, width=300),
        pn.Column(plot_histogram, plot_boxplot)
    ),
    plot_corr_matrix
)

dashboard.servable()
