# GCP_Log_Parser
 Process GCP4000 CP logs, extracting EZ, EX, and speed values into graphable form.

## Instructions
Run `01_ProcessGCPLogs.py` to process a GCP CP Log file into a csv file, containing EZ, EX, and speed values.

This CSV can then be used to plot the approach curve (EZ vs time) using either of the following methods:

1. Use Excel to manually plot create the plot

2. Run the XXX.py script to automatically generate a set of line plots



# Dependencies
External libraries can be installed by using the following command in the command prompt:
- pip install [Library_name]

### 01_ProcessGCPLogs.py
No external libraries necessary (only uses base python imports).

### 02_PlotApproachGraph.py
Requires the following external libraries:

1. Numpy
2. Pandas
3. matplotlib
4. Seaborn

