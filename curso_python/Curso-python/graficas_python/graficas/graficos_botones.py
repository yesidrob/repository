import pandas as pd
import plotly.graph_objects as go

datos = pd.read_excel('C:/Users/ADMIN/Desktop/workspace/datos local/Lista-de-clientes-con-nombre-y-direccion.xlsx')

conteo= datos['Grupo de clientes'].value_counts().reset_index()
conteo.columns = ['Grupos', 'Clientes']
conteo = conteo.sort_values(by='Grupos')

fig = go.Figure()


fig.add_trace(go.Bar(
    x=conteo['Grupos'],
    y=conteo['Clientes'],
    text=conteo['Clientes'],
    textposition='outside',
    marker=dict(color=['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightpink', 'lightyellow', 'lightgray']),
    visible=True,
    name='Barra',
    hoverlabel=dict(bgcolor='white',
                    font_size=14,
                    font_color= 'black',
                    font_family='Arial',
                    bordercolor='black',
                    ),
))

fig.add_trace(go.Pie(
    labels=conteo['Grupos'],
    values=conteo['Clientes'],
    textinfo='label+percent',
    name= 'Torta',
    marker=dict(line=dict(color=['black'], width=[0.5]),
                colors=['skayblue','lightgreen', 'lightcoral', 'lightsalmon', 'lightpink', 'lightyellow', 'lightgray']),
    visible=False,
    hoverlabel=dict(bgcolor='white',
                    font_size=14,
                    font_color= 'black',
                    font_family='Arial',
                    bordercolor='black',
                    
                    ),
))


fig.update_layout(
    updatemenus=[
        dict(
            direction='right',
            showactive=True,
            x=0.5,
            y=1.15,
            type='buttons',
            buttons=list([
                dict(label='Barra',
                     method='update',
                     args=[{'visible': [True, False]},
                           {"title":"Grupos de Clientes - Barra"}]),
                dict(label='Torta',
                     method='update',
                     args=[{'visible': [False, True]},
                           {"title":"Grupos de Clientes - Torta"}]),
            ]),
            
        ),
    ],
    title= 'Grupos de Clientes',
    xaxis_title= 'Grupos',
    yaxis_title= 'Clientes',
    font=dict(size=14, color='black', family='Arial'),
    paper_bgcolor='white',
    plot_bgcolor='white'
    )

fig.show()