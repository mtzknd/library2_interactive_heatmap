import streamlit as st

import pandas as pd

import plotly.express as px
import plotly.graph_objs as go

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv('lib2_data.csv')

df = load_data()

@st.cache_data
def pivot():
    return df.pivot_table(values='residual thrombin activity [%]', index = 'pool y', columns= 'pool x', sort=False)

data = pivot()

cmap = px.colors.sequential.PuRd_r

im = px.imshow(data, zmin=60, zmax = 100, color_continuous_scale= cmap)
im.update_traces(hovertemplate = 'None', hoverinfo='skip')

scat = im.add_trace(go.Scatter(mode ='markers', x = df['pool x'], y = df['pool y'], marker=dict(opacity=0)))

im.update_layout(height = 700)



col1, space, col2= st.columns((1,0.1,1))

with col1:
    st.title('Library 2 screening results')
    event = st.plotly_chart(im, on_select="rerun", use_container_width = True)
    selected_points = event.selection.points
    # st.write(selected_points)
    with col2:
        st.header('Instructions')
        st.write('Navigate and zoom heatmap using panel in the top right corner of the heatmap')
        st.write('Click on square in heatmap for monomer structures and raw data')

if len(selected_points) != 0:
    # st.write(selected_points)
    x1 = selected_points[0]['x']
    y1 = selected_points[0]['y']
    hoversrc = df[(df['pool x'] == x1) & (df['pool y'] == y1)]
    if len(hoversrc) != 0:  

        with col2:
            st.header('Monomers')
            col3, space3, col4, space4, col5, space5, col6 = st.columns((1,0.5,1,0.5,1,0.5,1)) 
        with col3:    
            for i in range(1,4):
                st.image("./mols/" + str(hoversrc['monomer %s' % str(i)].values[0])[1:] + '.png',
                caption=hoversrc['monomer %s' % str(i)].values[0])
        with col4:
            for i in range(4,7):
                st.image("./mols/" + str(hoversrc['monomer %s' % str(i)].values[0])[1:] + '.png', 
                         caption=hoversrc['monomer %s' % str(i)].values[0])
        with col5:
            for i in range(7,10):
                st.image("./mols/" + str(hoversrc['monomer %s' % str(i)].values[0])[1:] + '.png', 
                         caption=hoversrc['monomer %s' % str(i)].values[0])
        with col6:
            for i in range(10,13):
                st.image("./mols/" + str(hoversrc['monomer %s' % str(i)].values[0])[1:] + '.png', 
                         caption=hoversrc['monomer %s' % str(i)].values[0])

        with col2:
            st.header('Raw Data')
            st.write(hoversrc[['pool x', 'pool y', 'assay plate well', 'time0 (0 s)','time1 (150 s)','time2 (300 s)','time3 (450 s)','time4 (600 s)','time5 (750 s)','time6 (900 s)','slope','rvalue','residual thrombin activity [%]']].set_index(['pool x', 'pool y']))


