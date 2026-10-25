
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from palmerpenguins import load_penguins

# ==========================================
# 1. Page Setup
# ==========================================

st.set_page_config(
    page_title="Penguin Data Analysis Dashboard",
    page_icon="🐧",
    layout="wide"
)

st.title("Penguin Data Analysis Dashboard")
st.write(
    "Explore penguin species, body mass, "
    "flipper length, and other measurements."
)

# ==========================================
# 2. Load and Clean Dataset
# ==========================================

df = load_penguins()
df_clean = df.dropna().copy()

# ==========================================
# 3. Interactive Species Filter
# ==========================================

st.sidebar.header("Dashboard Filters")

species_options = sorted(df_clean["species"].unique())

selected_species = st.sidebar.multiselect(
    "Select penguin species",
    options=species_options,
    default=species_options
)

filtered_df = df_clean[
    df_clean["species"].isin(selected_species)
]

# ==========================================
# 4. Dashboard Metrics
# ==========================================

col1, col2 = st.columns(2)

col1.metric(
    "Original Dataset Rows",
    len(df)
)

col2.metric(
    "Filtered Penguin Records",
    len(filtered_df)
)

# ==========================================
# 5. Dataset Preview
# ==========================================

st.subheader("Dataset Preview")
st.dataframe(filtered_df.head(10), use_container_width=True)

# ==========================================
# 6. Chart 1: Species Count
# ==========================================

st.subheader("Chart 1: Number of Penguins by Species")

fig1, ax1 = plt.subplots(figsize=(8, 4))

sns.countplot(
    data=filtered_df,
    x="species",
    ax=ax1
)

ax1.set_xlabel("Penguin Species")
ax1.set_ylabel("Number of Penguins")
ax1.set_title("Penguin Count by Species")

st.pyplot(fig1)
plt.close(fig1)

# ==========================================
# 7. Chart 2: Body Mass Distribution
# ==========================================

st.subheader("Chart 2: Body Mass Distribution")

fig2, ax2 = plt.subplots(figsize=(8, 4))

sns.histplot(
    data=filtered_df,
    x="body_mass_g",
    bins=20,
    kde=True,
    ax=ax2
)

ax2.set_xlabel("Body Mass (grams)")
ax2.set_ylabel("Number of Penguins")
ax2.set_title("Distribution of Penguin Body Mass")

st.pyplot(fig2)
plt.close(fig2)

# ==========================================
# 8. Chart 3: Flipper Length vs Body Mass
# ==========================================

st.subheader("Chart 3: Flipper Length vs Body Mass")

fig3, ax3 = plt.subplots(figsize=(8, 4))

sns.scatterplot(
    data=filtered_df,
    x="flipper_length_mm",
    y="body_mass_g",
    hue="species",
    ax=ax3
)

ax3.set_xlabel("Flipper Length (mm)")
ax3.set_ylabel("Body Mass (grams)")
ax3.set_title("Flipper Length vs Body Mass")

st.pyplot(fig3)
plt.close(fig3)

# ==========================================
# 9. Summary
# ==========================================

st.subheader("Dataset Summary")

if not filtered_df.empty:
    st.write(
        "Average body mass:",
        f"{filtered_df['body_mass_g'].mean():.2f} grams"
    )
else:
    st.info("Select at least one species to display results.")
