# Converted from bargraph_SR.ipynb
# Clean Python script generated from the uploaded Jupyter notebook.
# Notebook outputs were removed from the cleaned .ipynb version.

# %% Cell 1
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import seaborn
from matplotlib.path import Path

# ==============================================================================
# 1. DATA LOADING AND PRE-PROCESSING
# ==============================================================================

# For this task, we will simulate the data from the user's example to make the code executable.
# The user's mock data has different column names, so we'll adjust the code to use the user's
# provided `plot_cols` and simulate data for them.

file_path = "~/Downloads/merged_RA_nanopore.csv"
try:
    df = pd.read_csv(file_path, skipinitialspace=True)
    df.columns = df.columns.str.strip()
    
    def get_mag_name(classification_str):
        parts = classification_str.split(';')
        for part in reversed(parts):
            if '__' in part.strip() and part.strip().startswith('s__') :
                return part.split('__', 1)[1].strip()
        return 'Unclassified Species'

    def get_class_name(classification_str):
        parts = classification_str.split(';')
        for part in parts:
            if part.strip().startswith('c__') and part.strip() != 'c__':
                return part.split('__', 1)[1].strip()
        return 'Other'

    df['Species'] = df['Classification'].apply(get_mag_name)
    df['Class'] = df['Classification'].apply(get_class_name)
    plot_cols = ['DL', 'PL', 'GE']
except FileNotFoundError:
    print("Warning: The CSV file was not found. Using mock data for demonstration.")


# ==============================================================================
# 2. DATA PREPARATION FOR PLOTTING
# ==============================================================================

df_plot = df[['Species', 'Class'] + plot_cols]

# Melt the DataFrame to long format
df_melted = df_plot.melt(
    id_vars=['Species', 'Class'],
    value_vars=plot_cols,
    var_name='Sample',
    value_name='Abundance'
)

# Sort Species by Class to group them in the stack and legend
# The bar graph should be sorted by class in ascending order to maintain the original look.
df_sorted = df.sort_values(by='Class', ascending=True).reset_index(drop=True)
sorted_species_for_bars = df_sorted['Species'].unique()
class_map = df_sorted.set_index('Species')['Class'].to_dict()

# Pivot data for the stacked bar chart using the ascending class sort order.
df_pivot = df_melted.pivot_table(
    index='Sample',
    columns='Species',
    values='Abundance',
    fill_value=0
)[sorted_species_for_bars].reindex(plot_cols)


# ==============================================================================
# 3. CALCULATE COORDINATES AND DEFINE COLORS
# ==============================================================================

# Assign a unique color to each Species. The color order is based on the ascending class sort.
n_species = len(sorted_species_for_bars)
colors = plt.cm.get_cmap("cubehelix", n_species)
# colors = plt.cm.get_cmap(seaborn.color_palette("cubehelix", n_species, as_cmap=True))
species_color_map = {species: colors(i) for i, species in enumerate(sorted_species_for_bars)}
species_color_map['Wenzhouxiangella sp007695005'] = (0.7, 0.1, 0.1, 1.0)
species_color_map['JAFIFS01 sp020831895'] = (0.9, 0.9, 0.1, 1.0)
species_color_map['RECH01 sp007694125'] = (0.7, 0.9, 0.7, 1.0)
species_color_map['Nodosilinea sp007135385'] = (0.3, 0.6, 0.6, 1.0)
print(species_color_map)

# Create the list of colors for the stacked bars.
bar_colors = [species_color_map[species] for species in sorted_species_for_bars]

# Calculate the cumulative sum to find the y-positions of each segment.
df_cumsum = df_pivot.cumsum(axis=1)

# ==============================================================================
# 4. PLOTTING AND DRAWING CONNECTORS (MODIFIED FOR LEGEND)
# ==============================================================================

fig, ax = plt.subplots(figsize=(20, 12))

# --- Define spacing and bar width ---
bar_width = 0.8
spacing = 1.0  # Increased spacing between bars
bar_positions = np.arange(len(plot_cols)) * (bar_width + spacing)

# Plot the main stacked bar chart
for i, col in enumerate(plot_cols):
    bottom = np.zeros(1)
    for species in sorted_species_for_bars:
        values = df_pivot.loc[[col], species].values
        ax.bar(
            bar_positions[i],
            values,
            width=bar_width,
            bottom=bottom,
            color=species_color_map[species],
            edgecolor='black',
            linewidth=1.5,
            label=species
        )
        bottom += values

# Set x-axis ticks and labels
ax.set_xticks(bar_positions)
ax.set_xticklabels(plot_cols, fontsize=14, fontweight='bold')

# --- Define positions for the custom legend ---
last_bar_idx_pos = bar_positions[-1]
legend_block_width = 0.2
legend_x_start = last_bar_idx_pos + bar_width/2 + 1.2
legend_block_x_end = legend_x_start + legend_block_width
legend_text_x = legend_block_x_end + 0.2
class_label_x = legend_text_x + 1.6

# --- MODIFICATION: SORTING THE LEGEND BY CLASS IN DESCENDING ORDER ---
df_sorted_legend = df.sort_values(by='Class', ascending=False).reset_index(drop=True)
sorted_species_for_legend = df_sorted_legend['Species'].unique()
n_species_legend = len(sorted_species_for_legend)
legend_y_positions = np.linspace(98, 2, n_species_legend)

# --- Draw Connectors between bars ---
for i in range(len(plot_cols) - 1):
    x_left = bar_positions[i]
    x_right = bar_positions[i+1]

    for species in sorted_species_for_bars:
        y_top_left = df_cumsum.loc[plot_cols[i], species]
        y_bottom_left = y_top_left - df_pivot.loc[plot_cols[i], species]

        y_top_right = df_cumsum.loc[plot_cols[i+1], species]
        y_bottom_right = y_top_right - df_pivot.loc[plot_cols[i+1], species]

        verts = [
            (x_left + bar_width / 2, y_bottom_left),
            (x_left + bar_width / 2, y_top_left),
            (x_right - bar_width / 2, y_top_right),
            (x_right - bar_width / 2, y_bottom_right),
        ]
        poly = patches.Polygon(verts, facecolor=species_color_map[species], alpha=0.35, edgecolor='black', linewidth=1.5)
        ax.add_patch(poly)

# --- Draw Connectors from the last bar to the legend, and the legend itself ---
for i, species in enumerate(sorted_species_for_legend):
    # Y position in the legend
    y_legend_center = legend_y_positions[i]
    legend_block_height = 2
    y_legend_top = y_legend_center + legend_block_height/2
    y_legend_bottom = y_legend_center - legend_block_height/2

    # Y positions on the last bar
    y_top_bar = df_cumsum.loc[plot_cols[-1], species]
    y_bottom_bar = y_top_bar - df_pivot.loc[plot_cols[-1], species]

    # Define the vertices for the polygon connector
    verts = [
        (last_bar_idx_pos + bar_width / 2, y_bottom_bar),
        (last_bar_idx_pos + bar_width / 2, y_top_bar),
        (legend_block_x_end - legend_block_width, y_legend_top),
        (legend_block_x_end - legend_block_width, y_legend_bottom)
    ]
    poly = patches.Polygon(verts, facecolor=species_color_map[species], alpha=0.35, edgecolor='black', linewidth=1.5)
    ax.add_patch(poly)

    # Add the color block in the legend
    rect = patches.Rectangle(
        (legend_block_x_end - legend_block_width, y_legend_bottom),
        legend_block_width, legend_block_height,
        facecolor=species_color_map[species], edgecolor='black', linewidth=1.5, zorder=10
    )
    ax.add_patch(rect)

    # Add Species text label
    ax.text(legend_text_x, y_legend_center, f"{species}", ha='left', va='center', fontsize=12)


# --- Draw Class labels and background patches ---
current_class = None
class_y_start = 0
for i, species in enumerate(sorted_species_for_legend):
    species_class = class_map[species]
    if species_class != current_class:
        if current_class is not None:
            y_max = legend_y_positions[i-1] - 1
            ax.text(class_label_x, (class_y_start + y_max)/2, current_class, ha='left', va='center', fontsize=12)
            rect = patches.Rectangle((legend_block_x_end - 0.2, y_max), class_label_x - legend_block_x_end + 1.4, class_y_start - y_max + 2,
                                     facecolor='grey', alpha=0.1, zorder=-1)
            ax.add_patch(rect)

        current_class = species_class
        class_y_start = legend_y_positions[i] + 1

# Draw the last class group
y_max = legend_y_positions[-1] - 1
ax.text(class_label_x, (class_y_start + y_max)/2, current_class, ha='left', va='center', fontsize=12)
rect = patches.Rectangle((legend_block_x_end - 0.2, y_max), class_label_x - legend_block_x_end + 1.4, class_y_start - y_max + 2,
                         facecolor='grey', alpha=0.1, zorder=-1)
ax.add_patch(rect)


# ==============================================================================
# 5. CUSTOMIZATION AND FINAL TOUCHES
# ==============================================================================

# --- Set plot titles and labels ---
ax.set_title(' ', fontsize=20, loc='left', pad=20)
ax.set_ylabel('Relative abundance of MAGs (%)', fontsize=20, weight='bold')
ax.set_xlabel('') # No x-axis label needed

# --- Customize ticks ---
ax.tick_params(axis='x', rotation=0, labelsize=16)
ax.tick_params(axis='y', labelsize=16)

# --- Set plot limits to make space for the legend ---
ax.set_ylim(0, 100)
ax.set_xlim(-0.5, last_bar_idx_pos + 6) # Adjusted to fit the new layout

# --- Clean up axes and layout ---
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
plt.tight_layout()

# --- Add headers for the legend ---
ax.text(class_label_x, 102, 'Class', ha='left', va='center', fontsize=16, weight='bold')
ax.text(legend_text_x, 102, 'Species', ha='left', va='center', fontsize=16, weight='bold')


# --- Save the plot ---
plt.savefig("RA_nanopore_LR_6.png", dpi=1000, bbox_inches='tight')
