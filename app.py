import streamlit as st

st.set_page_config(layout="wide", page_title="Ligand Discovery Protein Set Enrichment Analysis")

st.title('Welcome to Ligand Discovery!')

st.markdown("The Ligand Discovery data portal enables exploration of the largest fragment-based chemoproteomics screening to date.")

cols = st.columns(2)

col = cols[0]

col.header(":dart: [Interactions](https://example.com)")
col.markdown("Explore the interactions between ligands and proteins.")

col.header(":mag: [Explore protein sets](https://example.com)")
col.markdown("blabhblablabh")

col.header(":mountain: [Protein set enrichment analysis](https://example.com)")
col.markdown("blabhblablabh")

col.header(":robot_face: [Fragment predictor](https://example.com)")
col.markdown("blabhblablabh")

col.header(":rocket: [On-the-fly modeling](https://example.com)")
col.markdown("blabhblablabh")

col.header(":arrow_down: [Download data](https://example.com)")
col.markdown("blabhblablabh")

col = cols[1]
col.image("assets/fragments.jpeg", width=700)

st.divider()
st.subheader("About")
st.markdown("Ligand Discovery is a project to explore the interactions between ligands and proteins.")

st.subheader("FAQ")
st.write("blahblahblah")