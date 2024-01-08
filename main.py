import geopandas as gpd
import matplotlib.pyplot as plt

# Load shapefile
shapefile_path = './gis-map/districts.shp'
gdf = gpd.read_file(shapefile_path)

# Plot the map
gdf.plot()
plt.title('Map of Nepal - Districts')
plt.show()

# View attribute data
print(gdf.head())
