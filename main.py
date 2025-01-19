import re
from tkinter import filedialog
from os import getcwd


class Main:
    def __init__(self) -> None:
        # get user to select data file to import
        file_path_read = self.user_select_file()
        file_path_write = r'Output\processedLogData.csv'

        self.linesProcessed: int = 0

        with open(file_path_read, "r") as readFile:
            with open(file_path_write, "w") as writeFile:
                # add headings to file
                writeFile.write("DATE, TIME, TRACK NUM, EZ, EX, SPEED (mph), \n")

                self.processFileData(readFile, writeFile)

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
    
    # =======================================================================

    def processFileData(self, readFile, writeFile):
        while True:
            dataLine = readFile.readline()

            if dataLine == '': break    # check for end of file
            if self.checkDataLine(dataLine) == False: continue

            # break line of data into components and extract useful components
            parts = dataLine.split()
            dataList: list = self.groupTextFromParts(parts)

            self.writeProcessedData(writeFile, dataList)

    def writeProcessedData(self, writeFile, dataList):
        for data in dataList:
            writeFile.write(data)
            writeFile.write(", ")
        
        writeFile.write("\n")
        self.linesProcessed += 1
    
    # =======================================================================
        
    def checkDataLine(self, data: str) -> bool:
        # check 1
        pattern = r'CHK: '
        elements = re.findall(pattern, data)
        if len(elements) > 0:
            return False

        # check 2
        pattern = r'\bTrack | EZ: | EX: '
        elements = re.findall(pattern, data)
        if len(elements) >= 3:
            return True
        else:
            return False

    def groupTextFromParts(self, parts) -> list[str]:
        result = []

        # Manually group items based on positions or patterns
        # result.append(parts[0])       # e.g. "0E7"
        result.append(parts[1])         # e.g. "16APR24"
        result.append(parts[2])         # e.g. "16:47:29.9"
        result.append(f"{parts[3]} {parts[4]}")    # e.g. "Track 3"
        result.append(f"{parts[6]}")    # e.g. "EZ: 101"
        result.append(f"{parts[8]}")    # e.g. "EX: 98"
        if len(parts) > 9:              # e.g. "Speed: 82   mph"
            result.append(f"{parts[10]}")   
        else:
            result.append('')
        
        return result



# =======================================
def main():
    mainApp = Main()

    print(f"Number of data entries:\t{mainApp.linesProcessed}")
    print("=== Done ===")

if __name__ == "__main__":
    main()