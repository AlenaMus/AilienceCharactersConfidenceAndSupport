
import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Define parameters for the simulation and analysis.
NUM_ROWS = 5000
NUM_COLS = 6
SUPPORT_THRESHOLD = 0.30
CONFIDENCE_THRESHOLD = 0.70

# STEP 2: Define the names of the alien characteristics.
characteristics = [
    "Telepathic Emitters",      # Column 0
    "Acidic Blood",             # Column 1
    "Exoskeleton Plating",      # Column 2
    "Bioluminescent Skin",      # Column 3
    "Sonic Burst Capability",   # Column 4
    "Rapid Cellular Regeneration" # Column 5
]

# STEP 3: Generate the dataset with an INTENTIONAL CORRELATION.
print("Generating data with an artificial correlation...")
col1 = np.random.choice([0, 1], size=NUM_ROWS, p=[0.4, 0.6])
col2 = np.random.choice([0, 1], size=NUM_ROWS, p=[0.5, 0.5])
col4 = np.random.choice([0, 1], size=NUM_ROWS, p=[0.5, 0.5])
col5 = np.random.choice([0, 1], size=NUM_ROWS, p=[0.5, 0.5])
col3 = np.random.choice([0, 1], size=NUM_ROWS, p=[0.6, 0.4])
col6 = np.random.choice([0, 1], size=NUM_ROWS, p=[0.95, 0.05])
plating_indices = np.where(col3 == 1)[0]
num_to_regenerate = int(len(plating_indices) * 0.75)
regenerate_indices = np.random.choice(plating_indices, size=num_to_regenerate, replace=False)
col6[regenerate_indices] = 1

# STEP 4: Combine the individual columns into a single 2D NumPy array.
data = np.column_stack((col1, col2, col3, col4, col5, col6))
print(f"Generated a {data.shape[0]}x{data.shape[1]} array of alien characteristics.")

# STEP 4.5: Save the generated data matrix to a CSV file.
csv_filename = "alien_characteristics_matrix.csv"
header = ",".join(characteristics)
np.savetxt(csv_filename, data, delimiter=",", fmt='%d', header=header, comments='')
print(f"Successfully saved data matrix to '{csv_filename}'")


print("-" * 30)
print("Analyzing characteristic relationships...")
print(f"Minimum Support: {SUPPORT_THRESHOLD:.0%}")
print(f"Minimum Confidence: {CONFIDENCE_THRESHOLD:.0%}")
print("-" * 30)

# STEP 5: Perform Association Rule Mining and collect ALL rules.
all_rules = []
strong_rules = []

for i in range(NUM_COLS):
    for j in range(NUM_COLS):
        if i == j:
            continue

        antecedent_present = data[:, i] == 1
        consequent_present = data[:, j] == 1
        both_present_count = np.sum(antecedent_present & consequent_present)
        antecedent_count = np.sum(antecedent_present)
        consequent_count = np.sum(consequent_present)

        support = both_present_count / NUM_ROWS
        
        if antecedent_count == 0:
            confidence = 0
        else:
            confidence = both_present_count / antecedent_count

        # Calculate Lift
        support_antecedent = antecedent_count / NUM_ROWS
        support_consequent = consequent_count / NUM_ROWS
        if support_antecedent == 0 or support_consequent == 0:
            lift = 0
        else:
            lift = support / (support_antecedent * support_consequent)
        
        rule_data = {
            "antecedent": characteristics[i],
            "consequent": characteristics[j],
            "support": support,
            "confidence": confidence,
            "lift": lift
        }
        all_rules.append(rule_data)

        if support >= SUPPORT_THRESHOLD and confidence >= CONFIDENCE_THRESHOLD:
            strong_rules.append(rule_data)

print("\nAnalysis complete.")

# STEP 5.5: Print a summary of all strong relations found.
print("\n--- Summary of Strong Relations ---")
if strong_rules:
    for rule in strong_rules:
        print(f"- {rule['antecedent']} -> {rule['consequent']} (Support: {rule['support']:.2%}, Confidence: {rule['confidence']:.2%}, Lift: {rule['lift']:.2f})")
else:
    print("No strong relations were found that meet the specified thresholds.")
print("-" * 35)

# STEP 5.6: Display Full Table of All Relations
print("\n--- Full Table of All Possible Relations ---")
max_ant_len = max(len(rule['antecedent']) for rule in all_rules)
max_con_len = max(len(rule['consequent']) for rule in all_rules)

header = f"{'Antecedent':<{max_ant_len}} | {'Consequent':<{max_con_len}} | {'Support':>10} | {'Confidence':>12} | {'Lift':>8}"
print(header)
print("-" * len(header))

for rule in all_rules:
    print(f"{rule['antecedent']:<{max_ant_len}} | {rule['consequent']:<{max_con_len}} | {rule['support']:>9.2%} | {rule['confidence']:>11.2%} | {rule['lift']:>8.2f}")


# STEP 6: Visualize the results with a Scatter Plot.
print("\nGenerating visualization...")

if not all_rules:
    print("No rules were generated to visualize.")
else:
    supports = [rule['support'] for rule in all_rules]
    confidences = [rule['confidence'] for rule in all_rules]
    # Use Lift to color the points for a 3D effect
    lifts = [rule['lift'] for rule in all_rules]

    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(supports, confidences, c=lifts, cmap='viridis', alpha=0.7, label='All Rules')
    plt.colorbar(scatter, label='Lift')

    if strong_rules:
        strong_supports = [rule['support'] for rule in strong_rules]
        strong_confidences = [rule['confidence'] for rule in strong_rules]
        plt.scatter(strong_supports, strong_confidences, color='red', s=150, edgecolor='black', zorder=5, label='Strong Rules')
        for rule in strong_rules:
            plt.text(rule['support'], rule['confidence'], f"  {rule['antecedent']}\n  -> {rule['consequent']}", fontsize=9, zorder=6)

    plt.title('Association Rule Strength: Support vs. Confidence (Color by Lift)')
    plt.xlabel('Support')
    plt.ylabel('Confidence')
    plt.grid(True)
    
    plt.axhline(y=CONFIDENCE_THRESHOLD, color='r', linestyle='--', linewidth=0.8)
    plt.axvline(x=SUPPORT_THRESHOLD, color='g', linestyle='--', linewidth=0.8)
    plt.legend()
    
    output_filename = 'Ailience_Relations_Scatter_Plot.png'
    plt.savefig(output_filename)
    print(f"Successfully saved plot to '{output_filename}'")
