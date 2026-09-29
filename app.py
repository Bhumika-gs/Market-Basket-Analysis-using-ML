import streamlit as st
import pandas as pd
from pathlib import Path


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Market Basket Recommendation System",
    page_icon="🛒",
    layout="wide"
)


# --------------------------------------------------
# File Path
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
RULES_PATH = BASE_DIR / "data" / "association_rules.csv"


# --------------------------------------------------
# Load Rules
# --------------------------------------------------
@st.cache_data
def load_rules():
    return pd.read_csv(RULES_PATH)

rules = load_rules()


# --------------------------------------------------
# Recommendation Function
# --------------------------------------------------

def recommend_products(product, top_n=5):

    matching_rules = rules[
        rules["antecedents"].str.upper().str.contains(
            product.upper(),
            regex=False,
            na=False
        )
    ].copy()

    matching_rules = matching_rules.sort_values(
        by=["lift", "confidence"],
        ascending=False
    ).head(top_n)

    return matching_rules


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🛒 Market Basket Recommendation System")

st.markdown(
    """
    ### Discover products frequently purchased together

    This application uses **Association Rule Mining** and the
    **Apriori algorithm** to generate product recommendations.
    """
)

st.divider()


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.header("📊 Project Information")

st.sidebar.write(
    """
    **Dataset:** Online Retail

    **Transactions:** 18,019

    **Products:** 4,007

    **Algorithm:** Apriori

    **Rule Metrics:**
    - Support
    - Confidence
    - Lift
    """
)


# --------------------------------------------------
# Product Selection
# --------------------------------------------------

st.subheader("🔍 Find Product Recommendations")

products = sorted(
    rules["antecedents"]
    .dropna()
    .unique()
)

selected_product = st.selectbox(
    "Select a product:",
    products
)


# --------------------------------------------------
# Recommendation Button
# --------------------------------------------------

if st.button("🛒 Get Recommendations", type="primary"):

    result = recommend_products(
        selected_product,
        top_n=5
    )

    if result.empty:

        st.warning(
            "No recommendations found for this product."
        )

    else:

        st.success(
            f"Recommendations for: {selected_product}"
        )

        result = result.copy()

        result["confidence"] = (
            result["confidence"] * 100
        ).round(2)

        result["support"] = (
            result["support"] * 100
        ).round(2)

        result = result.rename(
            columns={
                "antecedents": "Product Bought",
                "consequents": "Recommended Product",
                "support": "Support (%)",
                "confidence": "Confidence (%)",
                "lift": "Lift"
            }
        )

        st.dataframe(
            result[
                [
                    "Product Bought",
                    "Recommended Product",
                    "Support (%)",
                    "Confidence (%)",
                    "Lift"
                ]
            ],
            use_container_width=True,
            hide_index=True
        )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Built using Python, Pandas, MLxtend, Apriori and Streamlit"
)
