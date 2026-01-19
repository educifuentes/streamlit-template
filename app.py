import streamlit as st


# ==========================================
# Page Configuration
# ==========================================
st.set_page_config(
    page_title="Spendee Dashboard :material/paid:",
    page_icon=":material/paid:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Section - Reports
overview_page = st.Page("pages/reports/1_overview.py", title="Overview", icon=":material/dashboard:")
details_page = st.Page("pages/reports/2_details.py", title="Details", icon=":material/inventory_2:")


# Section - Tools
uploads_page = st.Page("pages/tools/1_data_uploads.py", title="Data Uploads", icon=":material/upload_file:")
explore_page = st.Page("pages/tools/2_data_explorer.py", title="Data Explorer", icon=":material/search:")
documentation_page = st.Page("pages/tools/3_documentation.py", title="Documentation", icon=":material/book_2:")

style_page = st.Page("pages/guides/1_style.py", title="Style", icon=":material/palette:")
features_page = st.Page("pages/guides/2_features.py", title="Features", icon=":material/assignment_turned_in:")

# current page
pg = st.navigation({
    "Reports": [overview_page, details_page],
    "Tools": [uploads_page, explore_page, documentation_page],
    "Guides": [style_page, features_page]
})

# ==========================================
# Authentication
# ==========================================

from src.utils import check_password

# ==========================================
# Authentication
# ==========================================

if not check_password():
    st.stop()

pg.run()
