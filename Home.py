import osmnx as ox
import plotly.offline as pyo
import streamlit as st
from io import BytesIO
import requests

from PIL import Image

st.set_page_config(
    page_title="Home",
    layout="wide",
    initial_sidebar_state="expanded",
)

# IMG_URL = 'https://www.istockphoto.com/photo/3d-render-of-key-performance-indicators-business-concept-' \
#           'banner-gm1387135660-445156283?utm_source=unsplash&utm_medium=affiliate&utm_campaign=srp_photos_top' \
#           '&utm_content=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fbenchmarking&utm_term=benchmarking%3A%3A%3A' 

# IMG_URL = 'https://www.talkdesk.com/resources/reports/talkdesk-contact-center-kpi-benchmarking-report/'

# IMG_URL = 'https://www.talkdesk.com/resources/reports/talkdesk-contact-center-kpi' \
#           '-benchmarking-report/'

# IMG_URL = 'https://www.istockphoto.com/photo/on-the-table-are-a-notebook-a-pen-and-a-book-the-book-says-sustainability' \
#           '-gm1330264758-413737731?utm_source=unsplash&utm_medium=affiliate&utm_campaign=srp_photos_bottom&utm_content=https%' \
#           '3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fsustainability-kpi-reports&utm_term=sustainability%20kpi%20reports%3A%3A%3A' 

# IMG_URL = 'https://images.unsplash.com/photo-1492496913980-501348b61469?ixlib=rb-1.2.1&' \
#           'ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80/'

# IMG_URL = 'https://www.istockphoto.com/photo/on-the-table-are-a-notebook-a-pen-and-a-book-the-book-says-sustainability-gm1330264758-413737731?' \
#           'utm_source=unsplash&utm_medium=affiliate&utm_campaign=srp_photos_bottom&utm_content=https%3A%2F%2Funsplash.com%2Fs%2Fphotos' \
#           '%2Fsustainability-firm-reports&utm_term=sustainability%20firm%20reports%3A%3A%3A/'

# response = requests.get(IMG_URL)
# img = Image.open(BytesIO(response.content))

st.markdown("<h1 style='text-align: center; color: #4169e1;margin-top:-50px;'>STEMAWAY INTERNSHIP</h1>", unsafe_allow_html=True)
st.write("")
st.write("")
st.subheader('BUILDING A RECOMMENDER SYSTEM FOR DISCOURSE')
st.markdown('<h5>PROBELM STATEMENT:</h5>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns([4,0.1,0.2,2.5])

with col1:
    
    
    st.markdown("""
    What is Discourse?
    Discourse is the 100% open source discussion platform built for the next decade of the Internet. Use it as a\
    mailing list, discussion forum, long-form chat room, and more!\
    Discourse is a from-scratch reboot, an attempt to reimagine what a modern Internet discussion forum should be today,\
    in a world of ubiquitous smartphones, tablets, Facebook, and Twitter.
    Discourse's trust system means that the community builds a natural immune system to defend itself from trolls, bad actors,\
    and spammers — and the most engaged forum members can assist in the governance of their community. They put a trash can on\
    every street corner with a simple, low-friction flagging system. Positive behaviors are encouraged through likes and badges. \
    They gently, constantly educate members in a just-in-time manner on the universal rules of civilized discourse.
    
    The main problem is that Discourse plateform have not yet an efficient recommender system to help avoiding duplicate questions.\
    A recommender system that can recommend to a user when asking a question a similare question already answered will help people\
    trying to give answer to the same problem again and again without knowing. 
    
    Steps to be followed for a defined workflow :

    - Use stack overflow and Quora dataset for prototyping. \

    - Perform a web srapping on discourse plateform to validate our prototype.\

    - Build the final product as a pluging to add within discourse plateform.\
    
     
    """,  unsafe_allow_html=True)

# with col4:
    
#     st.image(img.resize((400, 500)))
