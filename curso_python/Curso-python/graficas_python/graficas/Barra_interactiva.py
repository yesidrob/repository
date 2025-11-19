import pandas as pd
import plotly.express as px

# Ejemplo de datos
datos = pd.read_excel('C:/Users/ADMIN/Desktop/workspace/datos local/Lista-de-clientes-con-nombre-y-direccion.xlsx', )
conteo= datos['Grupo de clientes'].value_counts().reset_index()
conteo.columns = ['Grupos', 'Clientes']
conteo= conteo.sort_values('Grupos')
barra= px.bar(conteo, x='Grupos', y='Clientes', color='Grupos', color_discrete_sequence=px.colors.qualitative.Pastel, title='Clientes por grupo')

barra.update_layout(
    
    title_font_size=24,
    title_font_family='Arial',
    title_font_color='black',
    plot_bgcolor='white',
    paper_bgcolor='#f9f9f9',
    xaxis_title='Grupos', 
    yaxis_title='Clientes',
    font=dict(
        family="Arial",
        size=14,
        color="black" ))

barra.update_traces(texttemplate='%{y}', textposition='outside', textfont_size=12, textfont_color='black',
                    hoverlabel=dict(bgcolor='white', font_size=12, font_family='Arial', font_color='black', bordercolor='black'))
barra.show()



