import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from IPython.display import Markdown


# new libraries for today:
#  geopandas is a library for working with geographical data
import geopandas as gpd
#  geoplot is a library for visualizing geographical data
import geoplot as gplt
#  we also will use a submodule of plotly
import plotly.graph_objects as go
#  networkx is a library for working with graphs and networks
import networkx as nx
# Pyvis is a library for drawing networks
from pyvis.network import Network
# another library, to be used for drawing graphs as a part of networkx


# Загрузка GeoJSON и преобразование координат
regions = gpd.read_file("slo_regions.geojson")
regions = regions.to_crs(epsg=4326)  # Конвертируем в WGS84

regions["dummy_value"] = 0 #данные 

# Создание карты
fig = px.choropleth(
    regions,
    geojson=regions.geometry,  # Геометрия после преобразования
    locations=regions.index,    # Индексы как идентификаторы регионов
    color="dummy_value",        # Столбец для цвета
    hover_name="NM3",           # Название региона при наведении
    projection="mercator"       # Проекция для EPSG:3857
)

# Настройка внешнего вида
fig.update_geos(
    fitbounds="locations",
    visible=False,
    bgcolor="#E0ECF4",          # Цвет фона
    showcountries=False,
    showocean=True,
)

fig.update_layout(
    title="карта Словакии",
    margin={"r": 0, "t": 40, "l": 0, "b": 0},
    coloraxis_showscale= True    # Скрыть шкалу цвета (так как данные фиктивные)
)

fig.show()