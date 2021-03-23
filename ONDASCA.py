#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk, filedialog, Text
import subprocess
import os
import time


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title(".:: ONDaSCA: On-demand Network Data Set Creation Application - GUI ::.")
        # self.minsize(640, 400)
        # self.wm_iconbitmap(open("icon.ico"))

        self.menu = Menu(self)
        self.config(menu=self.menu)
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label='Exit', command=self.quit)

        self.frame1 = ttk.LabelFrame(master=self, text="Realtime mode")
        self.frame1.pack(side=LEFT)

        self.frame2 = ttk.LabelFrame(master=self, text="Offline mode")
        self.frame2.pack(side=TOP)

        self.labelFrame = ttk.LabelFrame(self.frame2, text="Select Files")
        self.labelFrame.grid(column=1, row=1)

        self.labelFrame2 = ttk.LabelFrame(
            self.frame1, text="Select network interface")
        self.labelFrame2.grid(column=0, row=0, padx=10, pady=10)

        self.labelFrame3 = ttk.LabelFrame(
            self.frame1, text="Select capturing tool")
        self.labelFrame3.grid(column=1, row=0, padx=10, pady=10)

        self.labelFrame4 = ttk.LabelFrame(
            self.frame1, text="Select output directory")
        self.labelFrame4.grid(column=0, row=1, padx=10, pady=10)

        self.method = StringVar()
        self.interface = StringVar()

        Radiobutton(self.labelFrame3, text="Dumpcap",
                    variable=self.method, value="dumpcap").grid()
        Radiobutton(self.labelFrame3, text="Tshark",
                    variable=self.method, value="tshark").grid()

        self.inputfile = None
        self.outputdir = None

        self.button()
        self.button2()
        self.convertButton()
        self.captureButton()
        self.stopButton()

        self.getInterfaces()
        self.button3()

        self.pid = 100000

    def getInterfaces(self):
        self.getInterfaces = ttk.Label(self.labelFrame2)
        self.getInterfaces.grid(column=0, row=1)
        cmd = "ip -o link show | awk -F': ' '{print $2}'"
        p = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)

        try:
            i = 0
            for line in p.stdout:
                Radiobutton(self.labelFrame2, text=line.strip(
                ), variable=self.interface, value=line.strip()).grid(column=i, row=0)
                i += 1
        except:
            p.terminate()

    def button(self):
        self.button = ttk.Button(
            self.labelFrame, text="Browse Files", command=self.fileDialog)
        self.button.grid(column=1, row=1)
        self.entry = ttk.Entry(self.labelFrame, text="")
        self.entry.grid(column=0, row=1)

    def button2(self):
        self.button2 = ttk.Button(
            self.labelFrame, text="Select output directory", command=self.fileDialog2)
        self.button2.grid(column=1, row=2)
        self.entry2 = ttk.Entry(self.labelFrame, text="")
        self.entry2.grid(column=0, row=2)

    def button3(self):
        self.button3 = ttk.Button(
            self.labelFrame4, text="Select directory", command=self.fileDialog3)
        self.button3.grid(column=1, row=2)
        self.entry5 = ttk.Entry(self.labelFrame4, text="")
        self.entry5.insert(0, "testrun.pcap")
        # self.entry5.bind('<Button-1>', self.entry5.delete(0, END))
        self.inputfile = self.entry5.get()
        self.entry5.grid(column=0, row=1)
        self.entry4 = ttk.Entry(self.labelFrame4, text="")
        self.entry4.grid(column=0, row=2)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(
            initialdir='.', title='Select pcap file', filetypes=(("pcap", "*.pcap"), ("All", "*.*")))
        self.entry.configure(text=self.entry.insert(0, self.filename))
        self.inputfile = self.filename

    def fileDialog2(self):
        self.dirname = filedialog.askdirectory(
            initialdir=".", title="Select directory")
        self.entry2.configure(text=self.entry2.insert(0, self.dirname))
        self.outputdir = self.dirname

    def fileDialog3(self):
        self.dirname = filedialog.askdirectory(
            initialdir=".", title="Select directory")
        self.entry4.configure(text=self.entry4.insert(0, self.dirname))
        self.outputdir = self.dirname

    def convertButton(self):
        self.convertButton = ttk.Button(
            self.frame2, text="Start conversion", command=self.conversion)
        self.convertButton.grid(column=2, row=4)

    def captureButton(self):
        self.captureButton = ttk.Button(
            self.frame1, text="Start Capturing", command=self.conversion)
        self.captureButton.grid(column=1, row=2)

    def stopButton(self):
        self.stopButton = ttk.Button(
            self.frame1, text="Stop", command=self.stopCature)
        self.stopButton.grid(column=2, row=2)

    def pcapToCSV(self):
        self.cmd = "sudo cfm {0} {1}".format(self.inputfile, self.outputdir)
        self.p = subprocess.Popen(self.cmd, shell=True, stdout=True)
        self.entry3 = Text(master=self.frame1)
        self.entry3.insert("1.0", "Dataset creation started...\n")
        time.sleep(15)
        self.entry3.insert("2.0", "Dataset creation completed. Check {0}".format(self.outputdir))
        self.entry3.grid()
        return

    def stopCature(self):
        self.pid += 2
        os.system("sudo kill -9 {0}".format(self.pid))
        self.pcapToCSV()
        return

    def conversion(self):
        if not self.interface.get():
            if not self.inputfile:
                print(
                    "No interface or input pcap file selected. Please use the correct mode properly")
            else:
                if not self.outputdir:
                    print("Please select an output directory")
                else:
                    self.pcapToCSV()
        else:
            if not self.outputdir:
                print("Please select an output directory")
            else:
                cmd = "sudo {0} -i {1} -w {2}/{3}".format(self.method.get(), self.interface.get(), self.outputdir, self.inputfile)
                p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
                self.entry6 = Text()
                self.pid = p.pid
                self.inputfile = "{0}/{1}".format(self.outputdir, self.inputfile)
                self.output = p.stdout
              
                try:
                    return
                except (KeyboardInterrupt, SystemExit):
                    print("Interrupted detected")
                    p.kill()
                    print(self.inputfile)


if __name__ == '__main__':
    root = Root()
    root.mainloop()