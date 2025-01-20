from tkinter import filedialog
from os import getcwd

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



class Main:
    def __init__(self) -> None:
        file_path_read = self.user_select_file()

        df = pd.read_csv(filepath_or_buffer=file_path_read)

        



    # =======================================================================
    def user_select_file(self):
        filepath = filedialog.askopenfilename(
            initialdir=getcwd(),
            title = "Select GCP Log File for Processing",
            filetypes= (("log files", "*.log;*.txt"), ("All Files", "*.*"))
        )

        if filepath == "":
            print("No file selected. Exiting program.")
            exit()

        filename = filepath.split("/")[-1]
        print("File selected:", filename)
        return filepath
    





# =======================================
def main():
    mainApp = Main()

    print("=== Done ===")

if __name__ == "__main__":
    main()