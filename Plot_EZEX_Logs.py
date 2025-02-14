import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from tkinter import filedialog
from os import getcwd

def user_select_file():
        filepath = filedialog.askopenfilename(
            initialdir=getcwd(),
            title = "Select GCP Log File for Processing",
            filetypes= (("CSV files", "*.csv"), ("All Files", "*.*"))
        )

        if filepath == "":
            print("No file selected. Exiting program.")
            exit()

        filename = filepath.split("/")[-1]
        print("File selected:", filename)
        return filepath

file_path_read = user_select_file()

df = pd.read_csv(filepath_or_buffer=file_path_read)
df["DateTime"] = pd.to_datetime(df["DateTime"])
df.head()

df_data = df.copy()
trackNum = df_data.columns[2].split(" ")[0]
print("Track number:", trackNum)

newColNames = [
    "COUNT", 
    "DATE TIME", 
    "EZ", 
    "CHECK EZ",
    "EX",
    "PRIME",
    "DAX A",
]

df_data.columns = newColNames
df_data["TRACK NUM"] = trackNum
df_data


def plotApproachGraph(df_plot: pd.DataFrame):
    sns.set_theme(style="ticks")
    colors = sns.color_palette(palette='viridis', n_colors=10)
    alpha = 0.45

    fig, ax1 = plt.subplots(figsize=(20, 6))
    ax1.grid(True)
    
    x = "DATE TIME"
    y1 = "EZ"
    y2 = "DAX A"
    y3 = "PRIME"

    sns.lineplot(
        data=df_plot,
        x=x,
        y=y1,
        color=colors[0],
        # palette="flare",
        # hue="TRACK NUM",
        # style="TRACK NUM",
        marker="o",
        label="EZ value",
        ax=ax1,
        legend=False,
    )

    ax2 = ax1.twinx()
    sns.lineplot(
        data=df_plot,
        x=x,
        y=y2,
        color=colors[4],
        alpha=alpha,
        # palette="viridis",
        # hue="TRACK NUM",
        # style="TRACK NUM",
        # marker="o",
        linestyle='--',
        label=y2,
        ax=ax2,
        legend=False,
    )
    sns.lineplot(
        data=df_plot,
        x=x,
        y=y3,
        color=colors[8],
        alpha=alpha,
        # palette="viridis",
        # hue="TRACK NUM",
        # style="TRACK NUM",
        # marker="o",
        linestyle='--',
        label=y3,
        ax=ax2,
        legend=False,
    )

    # Fix the legend (since we're using two axes)
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc='lower left')
    

    # plt.legend()
    plt.title("Approach Graph", fontsize=22)
    plt.show()


df_plot = df_data
# df_plot = df_plot[df_plot['COUNT'] > 0]

plotApproachGraph(df_plot)
