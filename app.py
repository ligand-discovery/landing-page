import streamlit as st

st.set_page_config(layout="wide", page_title="Ligand Discovery Protein Set Enrichment Analysis")

st.title('Welcome to Ligand Discovery!')

st.markdown("The Ligand Discovery data portal enables exploration of the largest fragment-based chemoproteomics screening to date.")

cols = st.columns(2)

col = cols[0]

col.header(":dart: [Interactions](https://example.com)")
col.markdown("Explore the interactions between ligands and proteins. This is the main navigator to the chemoproteomics data, containing profiles for 407 fragments. The app also showcases competition assays for a few selected fragments.")

col.header(":mag: [Explore protein sets](https://example.com)")
col.markdown("With this tool, you can in put a set of proteins and see how many fragments interact with them according to our chemoproteomics data. We categorize proteins by their promiscuity/specificity levels to easily detect reported effect such as labeling bias.")

col.header(":mountain: [Protein set enrichment analysis](https://example.com)")
col.markdown("Explore fragment profiles from an enrichment perspective. We capture protein annotations of multiple scopes, from domains and families to molecular functions and cellular localization. We offer global and detailed views for each fragment.")

col.header(":robot_face: [Fragment predictor](https://example.com)")
col.markdown("Predict whether your fully-functionalized fragment of interest is likely to be promiscuous or associated with a specific interactome signature. We have predefined 10 interactome signatures capturing high-level biological processes that emerged from our chemoproteomics data.")

col.header(":rocket: [On-the-fly modeling](https://example.com)")
col.markdown("Build a machine learning model on the fly to predict potential interactions between your fully-functionalized fragments and proteins of interest. Sets of proteins are accepted and organized in coherent subsets to maximize the chance of obtaining a good model.")

col.header(":arrow_down: [Download data](https://example.com)")
col.markdown("Download our screening results for a more customized exploration.")

col = cols[1]
col.image("assets/fragments.jpeg", width=700)

st.divider()

st.subheader("Publication in _Science_")
st.markdown("This work is related to the following publication: [Offensperger et al., Science 384, eadk5864 (2024)](https://www.example.com).")

st.subheader("About")
st.markdown("Ligand Discovery is a project developed at [CeMM](https://cemm.at), Vienna, led by [Georg Winter](https://www.winter-lab.com/)'s group.")