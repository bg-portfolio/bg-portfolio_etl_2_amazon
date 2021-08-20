import streamlit as st
from utils.graph_controls import graph_controls
from utils.processing import load_dataframe, _connect_mongo
from streamlit.components.v1 import iframe


def fixed_content():
    """
    Contains fixed content visible across different links
    :return:
    """
    pass


def views(link):
    """
    Helper function for directing users to various pages.
    :param link: str,
    :return:
    """
    if link == 'Home':
        st.header("Welcome to The Projects' Dashboard!")
        st.subheader("Getting started")
        st.markdown("To create charts, wait for database connection, select a theme, "
                    "select a chart type, "
                    "set the chart options and download the chart.")
        st.sidebar.subheader('Settings')

        uploaded_file = _connect_mongo()

        fixed_content()
        if uploaded_file is not None:
            df, columns = load_dataframe(collection=uploaded_file)

            st.sidebar.subheader("Visualize your data")

            show_data = st.sidebar.checkbox(label='Show data')

            if show_data:
                try:
                    st.subheader("Data view")
                    number_of_rows = st.sidebar.number_input(
                        label='Select number of rows', min_value=2)

                    st.dataframe(df.head(number_of_rows))
                except Exception as e:
                    print(e)

            st.sidebar.subheader("Theme selection")

            theme_selection = st.sidebar.selectbox(label="Select your themes",
                                                   options=['plotly', 'plotly_white',
                                                            'ggplot2',
                                                            'seaborn', 'simple_white'])
            st.sidebar.subheader("Chart selection")
            chart_type = st.sidebar.selectbox(label="Select your chart type.",
                                              options=['Scatter plots', 'Line plots',
                                                       'Sunburst', 'Pie Charts',
                                                       'Histogram', 'Box plots', 'Tree maps', ])

            graph_controls(chart_type=chart_type, df=df,
                           dropdown_options=columns, template=theme_selection)
