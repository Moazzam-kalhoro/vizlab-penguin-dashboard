
# ==========================================
# VizLab Assignment
# Dataset: Palmer Penguins
# Task 1: Display the first and last rows
# ==========================================

import pandas as pd
from palmerpenguins import load_penguins

# Load the Palmer Penguins dataset
df = load_penguins()

# Display the first five rows
print("========== FIRST 5 ROWS ==========")
print(df.head())

# Display the last five rows
print("\n========== LAST 5 ROWS ==========")
print(df.tail())



# ==========================================
# Task 2: Check the Most Common Category
# ==========================================

# First, make a guess
print("\n========== TASK 2 ==========")
print("My guess: Adelie is the most common penguin species.")

# Count the number of penguins in each species
species_counts = df["species"].value_counts()

# Display the results
print("\nNumber of penguins in each species:")
print(species_counts)

# Display the most common species
print("\nMost common species:", species_counts.idxmax())
print("Number of penguins:", species_counts.max())



# ==========================================
# Task 3: Rows, Columns, and Data Types
# ==========================================

print("\n========== TASK 3 ==========")

# Check the number of rows and columns
print("Dataset shape (rows, columns):", df.shape)

# Check the number of rows
print("Number of rows:", df.shape[0])

# Check the number of columns
print("Number of columns:", df.shape[1])

# Check the data types and non-missing values
print("\nDataset information:")
df.info()

# Display the data type of every column
print("\nData types of each column:")
print(df.dtypes)



# ==========================================
# Task 4: Summary Statistics and Strange Values
# ==========================================

print("\n========== TASK 4 ==========")

# Select numerical columns
numeric_df = df.select_dtypes(include="number")

# Display summary statistics
print("\nSummary statistics:")
print(numeric_df.describe())

# Check the minimum and maximum of body mass
print("\nMinimum body mass (g):", df["body_mass_g"].min())
print("Maximum body mass (g):", df["body_mass_g"].max())

# Check the minimum and maximum of flipper length
print("\nMinimum flipper length (mm):", df["flipper_length_mm"].min())
print("Maximum flipper length (mm):", df["flipper_length_mm"].max())



# ==========================================
# Task 5: Top and Bottom 3 Records
# ==========================================

print("\n========== TASK 5 ==========")

# Sort penguins by body mass, from heaviest to lightest
print("\nTOP 3 HEAVIEST PENGUINS:")
print(
    df.sort_values(by="body_mass_g", ascending=False)
      .head(3)
)

# Sort penguins by body mass, from lightest to heaviest
print("\nBOTTOM 3 LIGHTEST PENGUINS:")
print(
    df.sort_values(by="body_mass_g", ascending=True)
      .head(3)
)



# ==========================================
# Task 6: Identify Missing Values
# ==========================================

print("\n========== TASK 6 ==========")

# Count missing values in each column
missing_counts = df.isnull().sum()

print("\nMissing values in each column:")
print(missing_counts)

# Calculate the percentage of missing values in each column
missing_percentages = (df.isnull().sum() / len(df)) * 100

print("\nPercentage of missing values in each column:")
print(missing_percentages.round(2))

# Display only columns that contain missing values
print("\nColumns with missing values:")
print(missing_percentages[missing_percentages > 0].round(2))



# ==========================================
# Task 7: Handle Missing Values
# ==========================================

print("\n========== TASK 7 ==========")

# Count rows before cleaning
print("Rows before cleaning:", len(df))

# Create a cleaned DataFrame by dropping rows with missing values
df_clean = df.dropna().copy()

# Count rows after cleaning
print("Rows after cleaning:", len(df_clean))

# Count rows removed
rows_removed = len(df) - len(df_clean)
print("Rows removed:", rows_removed)

# Confirm that no missing values remain
print("\nMissing values after cleaning:")
print(df_clean.isnull().sum())



# ==========================================
# Task 8: Check and Handle Duplicate Rows
# ==========================================

print("\n========== TASK 8 ==========")

# Count duplicate rows in the original dataset
duplicate_count = df.duplicated().sum()

print("Duplicate rows in original dataset:", duplicate_count)

# Explain our decision
if duplicate_count > 0:
    print("Decision: Remove duplicate rows to avoid repeated records.")
else:
    print("Decision: No duplicate rows found; no removal needed.")

# Remove duplicates from the cleaned dataset
df_clean = df_clean.drop_duplicates().copy()

print("Rows after removing duplicates:", len(df_clean))

# Verify that no duplicate rows remain
print("Duplicate rows remaining:", df_clean.duplicated().sum())



# ==========================================
# Task 9: Check for Invalid Values
# ==========================================

print("\n========== TASK 9 ==========")

# Select numerical measurement columns
measurement_columns = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g"
]

# Check for zero or negative measurements
for column in measurement_columns:
    invalid_count = (df_clean[column] <= 0).sum()

    print(f"{column}: {invalid_count} zero or negative values")

# Display rows containing any invalid measurements, if present
invalid_mask = (df_clean[measurement_columns] <= 0).any(axis=1)

print("\nRows containing invalid measurements:")
print(df_clean[invalid_mask])

# Explain our decision
if invalid_mask.any():
    print("\nDecision: Investigate and correct or remove invalid measurements.")
else:
    print("\nDecision: No zero or negative measurements found.")



# ==========================================
# Task 10: Detect Outliers Using IQR
# ==========================================

print("\n========== TASK 10 ==========")

# Select the body mass column and exclude missing values
body_mass = df_clean["body_mass_g"].dropna()

# Calculate the first and third quartiles
Q1 = body_mass.quantile(0.25)
Q3 = body_mass.quantile(0.75)

# Calculate the interquartile range
IQR = Q3 - Q1

# Calculate the lower and upper boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower boundary:", lower_bound)
print("Upper boundary:", upper_bound)

# Identify outliers
outliers = body_mass[
    (body_mass < lower_bound) |
    (body_mass > upper_bound)
]

print("\nNumber of body mass outliers:", len(outliers))
print("\nOutlier values:")
print(outliers.sort_values())

# Decision: report outliers, but do not automatically remove them
print("\nDecision: Keep the outliers for now and investigate them.")



# ==========================================
# Task 11: Histogram of Body Mass
# ==========================================

import matplotlib.pyplot as plt
import seaborn as sns

print("\n========== TASK 11 ==========")

# Create a histogram
plt.figure(figsize=(8, 5))

sns.histplot(
    data=df_clean,
    x="body_mass_g",
    bins=20,
    kde=True
)

plt.title("Distribution of Penguin Body Mass")
plt.xlabel("Body Mass (grams)")
plt.ylabel("Number of Penguins")

plt.tight_layout()
plt.show()



# ==========================================
# Task 12: Count Plot of Penguin Species
# ==========================================

print("\n========== TASK 12 ==========")

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df_clean,
    x="species"
)

plt.title("Number of Penguins by Species")
plt.xlabel("Penguin Species")
plt.ylabel("Number of Penguins")

plt.tight_layout()
plt.show()


# ==========================================
# Task 13: Box Plot of Body Mass by Species
# ==========================================

print("\n========== TASK 13 ==========")

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df_clean,
    x="species",
    y="body_mass_g"
)

plt.title("Body Mass Distribution by Penguin Species")
plt.xlabel("Penguin Species")
plt.ylabel("Body Mass (grams)")

plt.tight_layout()
plt.show()


# ==========================================
# Task 14: Scatter Plot
# ==========================================

print("\n========== TASK 14 ==========")

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df_clean,
    x="flipper_length_mm",
    y="body_mass_g",
    hue="species"
)

plt.title("Flipper Length vs Body Mass")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (grams)")

plt.tight_layout()
plt.show()


# ==========================================
# Task 15: Average Body Mass by Species
# ==========================================

print("\n========== TASK 15 ==========")

plt.figure(figsize=(8, 5))

sns.barplot(
    data=df_clean,
    x="species",
    y="body_mass_g",
    errorbar=None
)

plt.title("Average Body Mass by Penguin Species")
plt.xlabel("Penguin Species")
plt.ylabel("Average Body Mass (grams)")

plt.tight_layout()
plt.show()


# ==========================================
# Task 16: Correlation Heatmap
# ==========================================

print("\n========== TASK 16 ==========")

numeric_df = df_clean.select_dtypes(include="number")

correlation_matrix = numeric_df.corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap of Penguin Measurements")
plt.tight_layout()
plt.show()


# ==========================================
# Task 17: Improved Scatter Plot
# ==========================================

print("\n========== TASK 17 ==========")

plt.figure(figsize=(9, 6))

sns.regplot(
    data=df_clean,
    x="flipper_length_mm",
    y="body_mass_g",
    scatter=False,
    color="black"
)

sns.scatterplot(
    data=df_clean,
    x="flipper_length_mm",
    y="body_mass_g",
    hue="species",
    s=60
)

plt.title("Flipper Length vs Body Mass with Regression Line")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (grams)")
plt.legend(title="Penguin Species")

plt.tight_layout()
plt.show()


# ==========================================
# Task 18: Key Findings
# ==========================================

print("\n========== TASK 18 ==========")

print("1. The dataset contains 344 rows and 8 columns.")

print("2. Adelie is the most common penguin species.")

print("3. Missing values were found in bill measurements,")
print("   flipper length, body mass, and sex.")

print("4. After removing rows with missing values,")
print("   333 rows remained.")

print("5. Gentoo penguins have the highest average body mass.")

print("6. Flipper length and body mass show a positive relationship.")
