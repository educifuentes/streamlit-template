import streamlit as st

st.title("Style")

st.write("This is a style guide for the app.")

st.subheader("Icons")
st.markdown("use material icon fron [Material Symbols & Icons - Google Fonts](https://fonts.google.com/icons?selected=Material+Symbols+Outlined:book_2:FILL@0;wght@400;GRAD@0;opsz@24&icon.query=documentation&icon.size=24&icon.color=%23e3e3e3)")

st.code("use names of icon for example :material/dashboard:")

st.subheader("Usados frecuentemente")

favorites = '''
assignment_turned_in
dashboard
inventory_2
'''
st.code(favorites)

st.subheader("Colors")
st.markdown("Look up in Colorhunt website and use hex color")