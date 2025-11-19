import pandas as pd
import plotly.graph_objects as go

# Simulación de datos
conteo = pd.DataFrame({
    'Grupo': ['C', 'A', 'B'],
    'Clientes': [5, 12, 8]
})

# Ordenar grupos alfabéticamente y forzar orden
conteo = conteo.sort_values(by='Grupo')
conteo['Grupo'] = pd.Categorical(
    conteo['Grupo'],
    categories=sorted(conteo['Grupo'].unique()),
    ordered=True
)

# Crear figura vacía
fig = go.Figure()

# ===== Agregar trazas (gráficas diferentes) =====

# Gráfico de barras
fig.add_trace(go.Bar(
    x=conteo['Grupo'],
    y=conteo['Clientes'],
    name='Gráfico de Barras',
    marker_color='skyblue',
    text=conteo['Clientes'],
    textposition='outside',
    visible=True
))

# Gráfico de torta
fig.add_trace(go.Pie(
    labels=conteo['Grupo'],
    values=conteo['Clientes'],
    name='Gráfico de Torta',
    textinfo='percent+label',
    marker=dict(line=dict(color='black', width=1.5)),
    visible=False,
    hoverlabel=dict(bgcolor='white', 
                    font_size=14, 
                    font_family='Arial',
                    font_color='black'),
                    bordercolor='black',
    
))

# ===== Botones para alternar =====

fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            x=0.5,
            y=1.15,
            showactive=True,
            buttons=list([
                dict(label="Barras",
                     method="update",
                     args=[{"visible": [True, False]},
                           {"title": "Clientes por Grupo - Barras"}]),
                dict(label="Torta",
                     method="update",
                     args=[{"visible": [False, True]},
                           {"title": "Clientes por Grupo - Torta"}])
            ]),
        )
    ],
    title="Clientes por Grupo - Barras",
    xaxis_title="Grupo",
    yaxis_title="Cantidad de Clientes",
    font=dict(size=14),
    paper_bgcolor='white',
    plot_bgcolor='white',
    
)

fig.show()
