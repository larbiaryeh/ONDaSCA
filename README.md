# ONDaSCA
On-demand Network Data Set Creation Application for Network Intrusion Detection

## Requirements: 
•	Python3
•	Tkinter (python3-tk)
•	CICFlowmeter (https://github.com/ahlashkari/CICFlowMeter – installation requirements is provided)

The source code for this tools is provided as an attachment.

## ONDaSCA Capturing Modes
•	Realtime mode
•	Offline mode

### Realtime Mode
In the realtime mode, the user selects an interface to listen on, selects the capturing tool (dumpcap or tshark), inputs a file name in which the pcap file generated will be saved and also selects an output directory which by default is the current directory from which the tool is running from. Then the user can start capturing. 
The number of packets captured is displayed in the terminal in realtime. Once the packets captured reaches the desired number, the user can stop the capture. Once the capture is stopped, the pcap file is converted to a CSV format using CICFlowmeter and saved in the same directory with a .csv extension.

### Offline Mode
In a situation whereby the user already has a pcap file, the user can use the offline mode by selecting the pcap file as input and select an output directory which by default is the current directory in which the tool is running from and once the user clicks on Start conversion the tool generates the CSV from the pcap file using CICFlowmeter. 

## Data Set Creation Using Command Line Utility
The tool has also been designed to run as a command line tool. The source code for the command line version is also included as an attachment.

### Requirements
•	Python3
•	Argparse
•	CICFlowmeter (https://github.com/ahlashkari/CICFlowMeter – installation requirements is provided)

The command line tool provides the user the same capabilities as the GUI tool with the difference being that the command line version runs directly from the terminal and uses less system resources. 