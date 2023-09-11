import tkinter as tk
from tkinter import messagebox, Menu, Label, Entry
import re

# Existing code:
import socket
import time

def udpsocket1(msg, ip, port):
    sock.sendto(msg, (ip, port))

def udpsocket2(msg, ip, port):
    sock.sendto(msg, (ip, port))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 2000))

# Validate IP address
def validate_ip(ip):
    return re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', ip)

# Validate port number
def validate_port(port):
    try:
        port = int(port)
        return 1 <= port <= 65535
    except ValueError:
        return False

# Function to execute the socket commands
def execute_command():
    udp_ip1 = ip_entry1.get()
    udp_ip2 = ip_entry2.get()
    udp_port1 = port_entry1.get()
    udp_port2 = port_entry2.get()
    msg1 = message_entry1.get().encode()
    msg2 = message_entry2.get().encode()

    # Validations
    if not validate_ip(udp_ip1) or not validate_ip(udp_ip2):
        messagebox.showerror("Error", "Please enter valid IP addresses!")
        return
    if not validate_port(udp_port1) or not validate_port(udp_port2):
        messagebox.showerror("Error", "Please enter valid port numbers!")
        return

    print("In Progress")
    for i in range(3):
        udpsocket1(msg1, udp_ip1, int(udp_port1))
        udpsocket2(msg2, udp_ip2, int(udp_port2))
        time.sleep(.5)

    print("Complete")
    messagebox.showinfo("Info", "Command Executed Successfully!")

# Function to show the about dialog
def show_about_dialog():
    messagebox.showinfo("About", "Year: 2023\nLecture 4")

# GUI Creation:
root = tk.Tk()
root.title("Lecture 4")

menu_bar = Menu(root)
root.config(menu=menu_bar)

# Add 'Help' and 'Exit' Menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)  # Attach the File menu to the menu bar
file_menu.add_command(label="Exit", command=root.destroy)
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about_dialog)


# Message, IP, and Port Entry Widgets
label_msg1 = Label(root, text="UDP Message 1:")
label_msg1.pack(pady=5, padx=10)
message_entry1 = Entry(root, width=30)
message_entry1.insert(0, "Oh Wee Here we go!!!!!")
message_entry1.pack(pady=5, padx=10)

label1 = Label(root, text="Location 1 IP:")
label1.pack(pady=5, padx=10)
ip_entry1 = Entry(root)
ip_entry1.insert(0, "192.168.22.23")
ip_entry1.pack(pady=5, padx=10)

label_port1 = Label(root, text="Location 1 Port:")
label_port1.pack(pady=5, padx=10)
port_entry1 = Entry(root)
port_entry1.insert(0, "20")
port_entry1.pack(pady=5, padx=10)

label_msg2 = Label(root, text="UDP Message 2:")
label_msg2.pack(pady=5, padx=10)
message_entry2 = Entry(root, width=30)
message_entry2.insert(0, "What did I write Here")
message_entry2.pack(pady=5, padx=10)

label2 = Label(root, text="Location 2 IP:")
label2.pack(pady=5, padx=10)
ip_entry2 = Entry(root)
ip_entry2.insert(0, "192.168.33.23")
ip_entry2.pack(pady=5, padx=10)

label_port2 = Label(root, text="Location 2 Port:")
label_port2.pack(pady=5, padx=10)
port_entry2 = Entry(root)
port_entry2.insert(0, "20")
port_entry2.pack(pady=5, padx=10)

execute_btn = tk.Button(root, text="Execute Command", command=execute_command)
execute_btn.pack(pady=20)

root.mainloop()
