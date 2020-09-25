# ONDaSCA
On-demand Network Data Set Creation Application (ONDaSCA) is a customizable Data Set Application for Network Intrusion Detection. This application enables Network Administrators sniff network packet saved in the PCAP format and later converted to CSV for Machine Learning Algorithms. The application can be run on a firewall to generate realtime customised data set tailored to specific network. 

If you are using this for research purposes please cite our publication listed below. The bibtex is as follows.
## Requirements: 
<ul>
  <li>Python3</li>
  <li>Tkinter (python3-tk)</li>
  <li>CICFlowmeter (https://github.com/ahlashkari/CICFlowMeter – installation requirements is provided)</li>
 </ul>
  
## ONDaSCA Capturing Modes
<ul>
  <li>Realtime mode</li>
  <li>Offline mode</li>
 </ul>

### Realtime Mode
In the realtime mode, the user selects an interface to listen on, selects the capturing tool (dumpcap or tshark), inputs a file name in which the pcap file generated will be saved and also selects an output directory which by default is the current directory from which the tool is running from. Then the user can start capturing. 
The number of packets captured is displayed in the terminal in realtime. Once the packets captured reaches the desired number, the user can stop the capture. Once the capture is stopped, the pcap file is converted to a CSV format using CICFlowmeter and saved in the same directory with a .csv extension.

### Offline Mode
In a situation whereby the user already has a pcap file, the user can use the offline mode by selecting the pcap file as input and select an output directory which by default is the current directory in which the tool is running from and once the user clicks on Start conversion the tool generates the CSV from the pcap file using CICFlowmeter. 

## Data Set Creation Using Command Line Utility
The tool has also been designed to run as a command line tool. The source code for the command line version is also included as an attachment.

### Requirements
<ul>
  <li>Python3/li>
  <li>Argparse/li>
  <li>CICFlowmeter (https://github.com/ahlashkari/CICFlowMeter – installation requirements is provided)</li>
 </ul>

The command line tool provides the user the same capabilities as the GUI tool with the difference being that the command line version runs directly from the terminal and uses less system resources. 

## Reference for Citation
Aryeh, F.L. (2020). On-demand Network Data Set Creation Application (ONDaSCA). [online] GitHub. Available at: https://github.com/larbiaryeh/ONDaSCA [Accessed 24 Sep. 2020].
