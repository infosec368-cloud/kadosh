import subprocess
import tkinter as tk
from tkinter import messagebox

class PenetrationTestingTool:
    def __init__(self, master):
        self.master = master
        master.title("Penetration Testing Tool")

        self.label = tk.Label(master, text="Penetration Testing Tool")
        self.label.pack()

        self.nmap_button = tk.Button(master, text="Nmap Scan", command=self.nmap_scan)
        self.nmap_button.pack()

        self.vuln_button = tk.Button(master, text="Vulnerability Detection", command=self.detect_vulnerabilities)
        self.vuln_button.pack()

        self.metasploit_button = tk.Button(master, text="Metasploit Integration", command=self.run_metasploit)
        self.metasploit_button.pack()

    def nmap_scan(self):
        target = self.get_target()  # Implement target input method
        if target:
            subprocess.run(['nmap', target])
            messagebox.showinfo("Scan Complete", f"Nmap scan completed for {target}")

    def detect_vulnerabilities(self):
        # Placeholder for vulnerability detection logic
        messagebox.showinfo("Vulnerability Detection", "Vulnerability detection not implemented.")

    def run_metasploit(self):
        # Assuming Metasploit is installed and in PATH
        subprocess.run(['msfconsole'])
        messagebox.showinfo("Metasploit", "Metasploit launched.")

    def get_target(self):
        # Method to get target from user input
        return 'localhost'  # Placeholder for demo purposes

if __name__ == '__main__':
    root = tk.Tk()
    penetration_testing_tool = PenetrationTestingTool(root)
    root.mainloop()
