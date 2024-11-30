import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
from stl import mesh

# Function to create STL file
def create_stl_bulbs(filename, positions, radius):
    # Number of facets for sphere approximation
    n_facets = 20

    # Create a list to store all facets
    facets = []

    # Function to add a triangle to the facets list
    def add_triangle(v1, v2, v3):
        facets.append([v1, v2, v3])

    # Function to create a sphere at a given position
    def create_sphere(center, radius, n_facets):
        cx, cy, cz = center
        for i in range(n_facets):
            theta1 = i * 2 * np.pi / n_facets
            theta2 = (i + 1) * 2 * np.pi / n_facets
            for j in range(n_facets):
                phi1 = j * np.pi / n_facets
                phi2 = (j + 1) * np.pi / n_facets
                # Define four points of the facet
                p1 = (
                    cx + radius * np.sin(phi1) * np.cos(theta1),
                    cy + radius * np.sin(phi1) * np.sin(theta1),
                    cz + radius * np.cos(phi1),
                )
                p2 = (
                    cx + radius * np.sin(phi1) * np.cos(theta2),
                    cy + radius * np.sin(phi1) * np.sin(theta2),
                    cz + radius * np.cos(phi1),
                )
                p3 = (
                    cx + radius * np.sin(phi2) * np.cos(theta2),
                    cy + radius * np.sin(phi2) * np.sin(theta2),
                    cz + radius * np.cos(phi2),
                )
                p4 = (
                    cx + radius * np.sin(phi2) * np.cos(theta1),
                    cy + radius * np.sin(phi2) * np.sin(theta1),
                    cz + radius * np.cos(phi2),
                )
                # Create two triangles for each rectangular patch
                add_triangle(p1, p2, p3)
                add_triangle(p1, p3, p4)

    # Generate spheres for all positions
    for pos in positions:
        create_sphere(pos, radius, n_facets)

    # Convert facets to an array
    facets = np.array(facets)

    # Create the mesh object
    bulb_mesh = mesh.Mesh(np.zeros(facets.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(facets):
        for j in range(3):
            bulb_mesh.vectors[i][j] = f[j]

    # Save the mesh to an STL file
    bulb_mesh.save(filename)

# Function to calculate positions and generate STL
def generate_stl():
    try:
        # Get user inputs
        num_bulbs_x = int(entry_num_bulbs_x.get())
        num_bulbs_y = int(entry_num_bulbs_y.get())
        spacing_x = float(entry_spacing_x.get())
        spacing_y = float(entry_spacing_y.get())
        radius = float(entry_bulb_diameter.get()) / 2  # Radius = Diameter / 2
        height = float(entry_height.get())

        # Generate positions for bulbs
        positions = []
        amplitude = height / 4  # Set amplitude for wave function
        frequency_x = 2 * np.pi / (num_bulbs_x * spacing_x)
        frequency_y = 2 * np.pi / (num_bulbs_y * spacing_y)
        vertical_offset = height / 2

        for i in range(num_bulbs_x):
            for j in range(num_bulbs_y):
                x = i * spacing_x - (num_bulbs_x - 1) * spacing_x / 2
                y = j * spacing_y - (num_bulbs_y - 1) * spacing_y / 2
                z = amplitude * np.sin(frequency_x * x) * np.cos(frequency_y * y) + vertical_offset
                positions.append((x, y, z))

        # Ask user for save location
        filepath = filedialog.asksaveasfilename(defaultextension=".stl", filetypes=[("STL files", "*.stl")])
        if not filepath:
            return  # User canceled

        # Create the STL file
        create_stl_bulbs(filepath, positions, radius)
        messagebox.showinfo("Success", f"STL file created: {filepath}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the GUI
root = tk.Tk()
root.title("Wave STL Generator by Sinaholz.com")

# Input fields
tk.Label(root, text="Quantity of Bulbs in X:").grid(row=0, column=0, sticky="e")
entry_num_bulbs_x = tk.Entry(root)
entry_num_bulbs_x.grid(row=0, column=1)

tk.Label(root, text="Quantity of Bulbs in Y:").grid(row=1, column=0, sticky="e")
entry_num_bulbs_y = tk.Entry(root)
entry_num_bulbs_y.grid(row=1, column=1)

tk.Label(root, text="Distance of Bulbs in X (mm):").grid(row=2, column=0, sticky="e")
entry_spacing_x = tk.Entry(root)
entry_spacing_x.grid(row=2, column=1)

tk.Label(root, text="Distance of Bulbs in Y (mm):").grid(row=3, column=0, sticky="e")
entry_spacing_y = tk.Entry(root)
entry_spacing_y.grid(row=3, column=1)

tk.Label(root, text="Bulb Diameter (mm):").grid(row=4, column=0, sticky="e")
entry_bulb_diameter = tk.Entry(root)
entry_bulb_diameter.grid(row=4, column=1)

tk.Label(root, text="Height (mm):").grid(row=5, column=0, sticky="e")
entry_height = tk.Entry(root)
entry_height.grid(row=5, column=1)

# Generate button
generate_button = tk.Button(root, text="Generate STL", command=generate_stl)
generate_button.grid(row=6, column=0, columnspan=2)

# Start the GUI loop
root.mainloop()
