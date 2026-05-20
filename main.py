import streamlit as st
import sys
from pathlib import Path
import langchain_helper
# try:
#     import langchain_helper
# except ModuleNotFoundError:
#     st.error("langchain_helper module not found. Please ensure langchain_helper.py exists in the project directory.")
#     st.stop()

st.title("🍽️ Restaurant Name Generator")

cuisine = st.sidebar.selectbox(
    "Pick a Cuisine",
    ("Indian", "Italian", "Mexican", "Arabic", "American")
)

if cuisine:
    with st.spinner("Generating restaurant name and menu..."):
        response = langchain_helper.generate_restaurant_name_and_items(cuisine)

    st.header(response['restaurant_name'].strip())

    st.write("**Menu Items**")
    menu_items = response['menu_items'].strip().split(",")
    for item in menu_items:
        st.write("-", item.strip())