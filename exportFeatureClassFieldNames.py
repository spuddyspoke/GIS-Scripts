import arcpy
import pandas as pd

# Reference the current ArcGISPro project
aprx = arcpy.mp.ArcGISProject("CURRENT")

# Reference the correct map in the ArcGISPro project
# Note: Indexing starts at 0, so the first map is at index 0, the second at index 1, etc.
m = aprx.listMaps()[2]

# List all layers in the map
lyrs = m.listLayers()

# Create an empty list to hold the field names
# Create a dataframe to hold the list of field names for each layer
fieldNamesList = []
df = pd.DataFrame()

# Loop through each layer and get the field names and add them to the list
# Append each list of field names as a new row in the dataframe
for lyr in lyrs:
    fields = arcpy.ListFields(lyr)
    names = [field.name for field in fields]
    fieldNamesList.append(names)
    # Use the layer name (without the "GIS_EDITOR." prefix) as the column name
    # Adjust as needed based on your layer name structure
    col = arcpy.Describe(lyr).name[11:]
    df = df.append(pd.Series(names, name=col), ignore_index=False)
    # print(col)
    # print(len(names))
    # print(names)

# Transpose the dataframe so that each column is a layer and each row is a field name
df = df.transpose()
# print(df)

# Export the dataframe to a CSV file
# Adjust the file path as needed
# df.to_csv(r"Z:\Temp\Emily\ParksData_Fields.csv", index=False)
df.to_csv(r"PATH", index=False)