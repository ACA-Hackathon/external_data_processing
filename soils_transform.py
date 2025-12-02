import os
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely import Point


def print_a_map(gpd, column_name):
    """
    A miscellaneous function to do a visual check of the traetment
    """
    os.makedirs("tmp", exist_ok=True)
    gpd.plot(figsize=(15, 15),
             column=column_name,
             legend=True,
             s=0.05)
    plt.tight_layout()
    plt.savefig(f"tmp/{column_name}_map.png")

def pandas_df_to_parquet(df, path):
    df.to_parquet(path,
                  engine="pyarrow",
                  index=True)

def create_df_from_points(grid):
    points = gpd.GeoDataFrame({"lon": grid["lon"], "lat": grid["lat"]},
                              geometry=[Point(x, y) for x, y in zip(grid["lon"], grid["lat"])],
                              crs="EPSG:4326"
                              )
    return points

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    os.makedirs("tmp", exist_ok=True)
    SOIL_DB_PATH = "src/soils/shapes/30169_L93.shp"
    GRID_PATH = "src/grid.npz"
    STU_SMU_PATH = "src/soils/stuorg.csv"
    STU_INFO_PATH  = "src/soils/stu.csv"

    bdgsf = soils = gpd.read_file(SOIL_DB_PATH)
    grid = np.load(GRID_PATH)
    stu_smu = pd.read_csv(STU_SMU_PATH, sep=";")
    stu_info = pd.read_csv(STU_INFO_PATH, sep=";")

    bdgsf = bdgsf.to_crs("EPSG:4326")
    points = create_df_from_points(grid)
    appartenance = gpd.sjoin(points, bdgsf,
                             how="inner",
                             predicate="within")
    appartenance_simple = appartenance[["lon", "lat", "SMU", "geometry"]]

    stu_info = stu_info.loc[:, ["stu", "soil", "soil90", "text1", "text2",
                                "slope1", "slope2", "aglim1", "aglim2",
                                "mat1", "mat2", "zmin", "zmax",
                                "use1", "use2", "dt", "td1", "td2",
                                "roo", "il", "wr", "wm1", "wm2",
                                "wm3", "cfl"]]
    
    df_final = pd.merge(appartenance_simple,
                        stu_smu.loc[:, ["smu", "stu"]],
                        left_on="SMU",
                        right_on="smu",
                        how="left")
    
    df_final = pd.merge(df_final,
                        stu_info,
                        left_on="stu",
                        right_on="stu",
                        how="left")
    print_a_map(gpd=df_final, column_name="soil")

    df_final = pd.DataFrame(df_final.drop(columns=["geometry"]))

    pandas_df_to_parquet(df_final, "data/soils.parquet")