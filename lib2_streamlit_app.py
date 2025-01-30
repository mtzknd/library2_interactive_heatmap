import streamlit as st

import pandas as pd

import plotly.express as px
import plotly.graph_objs as go

st.set_page_config(layout="wide")

@st.cache_data
def load_excel_sheet():
    return pd.read_excel(io='lib2_data.xlsx', engine='openpyxl')

df = load_excel_sheet()

@st.cache_data
def pivot():
    return df.pivot_table(values='res act', index = 'pool_id_2', columns= 'pool_id_1', sort=False)

data = pivot()

cmap = px.colors.sequential.PuRd_r

im = px.imshow(data, zmin=60, zmax = 100, color_continuous_scale= cmap)
im.update_traces(hovertemplate = 'None', hoverinfo='skip')

scat = im.add_trace(go.Scatter(mode ='markers', x = df['pool_id_1'], y = df['pool_id_2'], marker=dict(opacity=0)))

im.update_layout(height = 600)

col1, col2, col3, col4, col5 = st.columns((4,1,1,1,1))

with col1:
    st.title('Library 2 screening results')
    event = st.plotly_chart(im, on_select="rerun", use_container_width = True)
    selected_points = event.selection.points
    # st.write(selected_points)

if len(selected_points) != 0:
    # st.write(selected_points)
    x1 = selected_points[0]['x']
    y1 = selected_points[0]['y']
    hoversrc = df[(df['pool_id_1'] == x1) & (df['pool_id_2'] == y1)]
    if len(hoversrc) != 0:  
        with col1:
            st.write(hoversrc[['pool_id_1', 'pool_id_2', 'assayplate_well', 'time0', 'time1', 'time2', 'time3', 'time4', 'time5', 'time6', 'slopes', 'rvalue', 'res act']].set_index(['pool_id_1', 'pool_id_2']))
        with col2:
            for i in range(1,4):
                st.image("./mols/" + str(hoversrc['pep%s' % str(i)].values[0]) + '.jpg',
                caption=hoversrc['pep%s' % str(i)].values[0])
        with col3:
            for i in range(4,7):
                st.image("./mols/" + str(hoversrc['pep%s' % str(i)].values[0]) + '.jpg', 
                         caption=hoversrc['pep%s' % str(i)].values[0])
        with col4:
            for i in range(7,10):
                st.image("./mols/" + str(hoversrc['pep%s' % str(i)].values[0]) + '.jpg', 
                         caption=hoversrc['pep%s' % str(i)].values[0])
        with col5:
            for i in range(10,13):
                st.image("./mols/" + str(hoversrc['pep%s' % str(i)].values[0]) + '.jpg', 
                         caption=hoversrc['pep%s' % str(i)].values[0])

