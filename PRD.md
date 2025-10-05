# Product Requirements Document (PRD): Alien Character Analysis Script

## 1. Objective

The primary objective of this program is to serve as a self-contained, educational tool to demonstrate the principles of **Association Rule Mining** on a synthetic dataset. It is designed to find and quantify relationships between variables (alien characteristics) using only the `numpy` library for core calculations, proving the concepts of Support, Confidence, and Lift from first principles.

## 2. Features & Functionality

### 2.1. Core Features

- **F1: Synthetic Data Generation**: The system shall generate a 2D `numpy` array of a specified size (5000 rows, 6 columns) representing a population of aliens. Each value shall be binary (0 or 1).
- **F2: Probabilistic Trait Distribution**: The data generation shall allow for specific columns to have unique probabilities of being `1` (e.g., 60%, 40%, 25%).
- **F3: Intentional Correlation**: To ensure a demonstrable result, the system shall artificially create a strong positive correlation between at least two characteristics.
- **F4: Association Rule Calculation**: The system must calculate the following metrics for every possible directional relationship between characteristics (A -> B):
    - **Support**: The frequency of (A and B) in the dataset.
    - **Confidence**: The probability of B given A.
    - **Lift**: The correlation between A and B compared to random chance.
- **F5: Data Export**: The system shall save the complete generated data matrix to a persistent, human-readable format (`.csv`).
- **F6: Results Visualization**: The system shall generate a 2D scatter plot to visualize the relationship between Support and Confidence for all rules. The plot must use a third dimension (color) to represent Lift.

### 2.2. User Interaction

- **UI1: Command-Line Interface**: The program will be executed via a single command-line instruction (`python <script_name>.py`).
- **UI2: Console Reporting**: All analytical results, including summaries and full data tables, shall be printed to the console in a formatted, readable manner.

## 3. User Flow

1.  The user executes the Python script from their terminal.
2.  The script prints status updates to the console as it generates data and performs the analysis.
3.  The script outputs a summary of strong relations and a full table of all relations to the console.
4.  The script saves two files to the local directory: `alien_characteristics_matrix.csv` and `Ailience_Relations_Scatter_Plot.png`.
5.  The user can inspect the console output, open the CSV file for the raw data, and view the PNG image for the visualization.

## 4. Success Metrics

- The program runs to completion without errors.
- The program correctly identifies and prints the artificially created strong relationship with Support >= 30% and Confidence >= 70%.
- The `alien_characteristics_matrix.csv` and `Ailience_Relations_Scatter_Plot.png` files are created successfully in the correct location and are not corrupted.
