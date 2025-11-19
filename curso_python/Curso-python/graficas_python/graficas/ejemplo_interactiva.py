import pandas as pd
import plotly.express as px

# Datos simulados
conteo = pd.DataFrame({
    'Grupo': ['A', 'B', 'C'],
    'Clientes': [12, 8, 5]
})

fig = px.bar(
    conteo,
    x='Grupo',
    y='Clientes',
    title='Clientes por Grupo',
    color='Grupo',
    color_discrete_sequence=px.colors.qualitative.Pastel
)

# Estética
fig.update_layout(
    width=800,
    height=500,
    title_font_size=24,
    title_font_family='Arial',
    xaxis_title='Grupo de Clientes',
    yaxis_title='Cantidad de Clientes',
    xaxis_tickangle=0,
    plot_bgcolor='white',
    paper_bgcolor='#f9f9f9',
    font=dict(size=14, color='black'),
    legend_title_text='Grupo'
)

# Mostrar número en cada barra
fig.update_traces(text=conteo['Clientes'], textposition='outside')

# Mostrarlo
fig.show()
