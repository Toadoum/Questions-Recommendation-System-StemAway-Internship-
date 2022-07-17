import streamlit as st

st.set_page_config(
    page_title="About",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.header("Timeline")

st.subheader("Overview")

st.markdown(f'Timeline from the Start of the Week: ')

st.markdown('<h3 style=color:#4169e1;">Week 1-3</h1>', unsafe_allow_html=True)

st.markdown(""" 
* Training
* Litterature review
* Figuring out the approach to perform web scraping
* Look for online dataset for prototype
""", unsafe_allow_html=True)

st.markdown('<h3 style=color:#4169e1;">Week 4-8</h1>', unsafe_allow_html=True)

st.markdown(""" 
* Identifying our target, minimum and maximum goal
* Explore model to finetune (Natural Language Inference, Semantic Textual Similarity, Paraphrase Data etc.)
* Build a prototype using Stack overflow and Quora dataset
* Test the prototype using pinecone
* Design a presentation to pitch about the prototype
* Perform web scrapping on Discourse plateform (Data collection and preprocessing).
* Adapt our model using Discourse dataset.
* Work on our minimum Goal and testing
* Maximum goal and testing
* Final report and presentation
""", unsafe_allow_html=True)


