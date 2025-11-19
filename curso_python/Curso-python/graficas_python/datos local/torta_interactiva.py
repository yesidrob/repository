import pandas as pd
import plotly.express as px

datos = pd.read_excel('C:/Users/ADMIN/Desktop/workspace/datos local/Lista-de-clientes-con-nombre-y-direccion.xlsx')

conteo = datos['Grupo de clientes'].value_counts().reset_index()
conteo.columns = ['Grupos', 'Clientes']
conteo = conteo.sort_values(by='Grupos')


torta = px.pie(conteo, values='Clientes', names='Grupos',
                title='Distribución de clientes por grupo',
                color_discrete_sequence=px.colors.qualitative.Pastel)

torta.update_traces(textfont_size=14,
                    hoverinfo='label+percent+value',
                    pull=[0.05, 0, 0],
                    textinfo='percent+label',
                    hoverlabel=dict(bgcolor='white', 
                                    font_size=14, 
                                    font_family='Arial',
                                    bordercolor='black',
                                    font_color='black'),
                    marker=dict(line=dict(color='black', width=0.5)))

torta.update_layout(showlegend=True,
                    paper_bgcolor='white',
                    plot_bgcolor='white',
                    legend_title_text='Grupos',
                    font=dict(size=14, color='black'))

torta.show()