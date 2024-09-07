import tkinter as tk
from tkinter import ttk
import json

# Load YAML templates from JSON file
def load_yaml_templates():
    with open('yaml_templates.json', 'r') as file:
        return json.load(file)

yaml_templates = load_yaml_templates()

# Create the main application window
root = tk.Tk()
root.title("Kubernetes Components Viewer")

# Set up the left frame for the tree view
left_frame = tk.Frame(root, width=300)
left_frame.pack(side=tk.LEFT, fill=tk.Y)

# Set up the right frame for the YAML display
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Create a tree view for Kubernetes components
tree = ttk.Treeview(left_frame)
tree.heading("#0", text="Kubernetes Components")
tree.pack(fill=tk.BOTH, expand=True)

# Create a text widget for displaying YAML
yaml_display = tk.Text(right_frame, wrap=tk.NONE)
yaml_display.pack(fill=tk.BOTH, expand=True)

# Function to populate the tree view with folders and items
def populate_tree():
    # Define the folders and their components
    folders = {
        "Workloads": [
            "Deployments",
            "StatefulSets",
            "DaemonSets",
            "ReplicaSets",
            "Jobs",
            "CronJobs"
        ],
        "Networking": [
            "Services",
            "Ingresses",
            "NetworkPolicies"
        ],
        "Storage": [
            "PersistentVolumes",
            "PersistentVolumeClaims",
            "StorageClasses"
        ],
        "Configuration and Storage": [
            "ConfigMaps",
            "Secrets"
        ],
        "Cluster Management": [
            "Nodes",
            "Namespaces",
            "ResourceQuotas"
        ],
        "Monitoring and Logging": [
            "Events",
            "PodDisruptionBudgets"
        ]
    }
    
    for folder, components in folders.items():
        # Add folder to the tree
        folder_id = tree.insert("", tk.END, text=folder, open=True)
        for component in components:
            tree.insert(folder_id, tk.END, text=component)

populate_tree()

# Function to update YAML display based on selected tree item
def on_tree_select(event):
    selected_item = tree.selection()[0]
    component_name = tree.item(selected_item, "text")
    
    # Find the corresponding YAML template
    yaml_content = yaml_templates.get(component_name, "No YAML available")
    
    yaml_display.delete(1.0, tk.END)
    yaml_display.insert(tk.END, yaml_content)

# Bind tree selection event to the handler
tree.bind("<<TreeviewSelect>>", on_tree_select)

root.mainloop()
