from uv_wrapper import Pattern
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create control_pattern.png
check_object = Pattern(height=1024, width=1024, radius=64)  #
path = check_object.create_control("control_pattern")
# Calculate the origins of the blobs with cv moments method
centers_control = check_object.get_blob_center(path)
# Calculate angles and distances

dh_control,ah_control = check_object.horizontal_da(centers_control)
dv_control,av_control = check_object.vertical_da(centers_control)

centers_distorted = check_object.get_blob_center("pattern_distorted_1.png")

dh_distorted,ah_distorted = check_object.horizontal_da(centers_distorted)
dv_distorted,av_distorted = check_object.vertical_da(centers_distorted)


error_distances_horizontal = dh_distorted - dh_control
error_distances_vertical = dv_distorted - dv_control
error_angles_horizontal = ah_distorted -  ah_control
error_angles_vertical = av_distorted - av_control


# Distort control_pattern.png

# Analise the data into pandas

# creating a plot of the centers
df_centers = pd.DataFrame(centers_distorted, columns=["x", "y"])

sns.set_theme()
sns.set_context("paper")
#sns.histplot(data=error_distances_vertical)
sns.histplot(error_distances_horizontal)

# sns.scatterplot(x=df_centers["x"], y=df_centers["y"])
# plt.scatter(centers_distorted[12][0], centers_distorted[12][1], marker='o', color="green", s=100)
# plt.scatter(centers_distorted[13][0], centers_distorted[13][1], marker='o', color="red", s=100)
# plt.scatter(centers_distorted[11][0], centers_distorted[11][1], marker='o', color="red", s=100)

plt.show()

