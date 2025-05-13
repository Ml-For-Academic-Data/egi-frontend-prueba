import panel as pn
import pandas as pd
import os

pn.extension()

df = pd.read_csv("../processed/cleaned_data.csv")

scatter = pn.pane.Plotly({
    'data': [{'x': df['promedio'], 'y': df['asistencia'], 'mode': 'markers', 'type': 'scatter'}],
    'layout': {'title': 'Promedio vs Asistencia'}
})

histogram = pn.pane.Plotly({
    'data': [{'x': df['edad'], 'type': 'histogram'}],
    'layout': {'title': 'Distribución de Edades'}
})

template = pn.template.MaterialTemplate(title="Dashboard de Deserción Estudiantil")
template.sidebar.append(pn.pane.Markdown("### Información"))
template.main.append(pn.Row(scatter, histogram))

if __name__ == "__main__":
    template.show(port=5006)