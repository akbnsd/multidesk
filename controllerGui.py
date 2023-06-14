import tkinter as tk

root = None
host_listbox = None
openStreamingWindow = lambda a : a

def renderGui():
    global root, host_listbox
    root = tk.Tk()
    root.title("Host Controller")

    
    # Create the host listbox
    host_listbox = tk.Listbox(root)
    host_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create the scrollbar for the host listbox
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the scrollbar for the host listbox
    host_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=host_listbox.yview)
        
    # Create the connect button
    connect_button = tk.Button(root, text="Connect", command=openStreamingWindow)
    connect_button.pack(side=tk.BOTTOM, padx=10, pady=10)
    root.mainloop()


# Function to handle the selection of a host from the list


# Function to establish a TCP connection with a selected host
def connect_to_host(host):
    # Extract the host address and port from the selected host string
    host_address, host_port = host.split(':')

    # Establish a TCP connection with the host
    # Implement the necessary logic to establish the connection

# Create the main window
# Start the GUI event loop
