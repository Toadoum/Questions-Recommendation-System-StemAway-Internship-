import streamlit as st

st.set_page_config(
    page_title="About",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.header("Tasks Progress")

#st.markdown(f'Task 1:')

st.markdown('<h2 style=color:#4169e1;">General Discussion</h2>', unsafe_allow_html=True)

#st.markdown('<h3 style=color:#4169e1;">Progress Made</h1>', unsafe_allow_html=True)

st.markdown(""" 
The first meeting was to discuss about the general idea of the project and draft something.\

* Main Points
Recommender systems paradigms: Matrix factorization and Semantic Similarity measures.\

* Base-plan:
Use sentence-BERT 1 to compute topic vectors Compare results with TF-IDF for discourse/stackExchange API’s Add-ons:
Use multi-modal transformers to inject structured data (time, visits count, etc) and act as s supervisory signal
Use Pincode for adding the structured data in a post modeling fashion as well as for optimized deployment.\

* Future Considerations
A literature review is to be made and both should be compared and contrasted:
Exploring actual encoding mechanism E.g: sentence-BERT, prompt-BERT, xDeepFM…etc
Combining structural data with text E.g: Multi-modal transformer, Pinecode…etc
Recommender system loop: How these systems work from start to finish and specifically for the “recommender” backbone, 
whether it uses a multi stage process or not Supervisory signals nature and addition (what type of structured data can we use?)\

* Exploratory Teams
Help with data cleaning and preparation; getting the data in the ‘right’ form for more deep models Web-scrapping for similar topics 
sets This dataset [Stack Overflow Data | Kaggle 5] can be used as an example of what we would like to work with.
""", unsafe_allow_html=True)

#st.markdown('<h3 style=color:#4169e1;">Next Steps</h1>', unsafe_allow_html=True)



st.markdown('<h3 style=color:#4169e1;">References</h1>', unsafe_allow_html=True)

st.markdown(""" 
* Prompt BERT: https://github.com/kongds/Prompt-BERT
* Paper about prompt Bert: https://arxiv.org/pdf/2201.04337.pdf
* Multimodal : https://multimodal-toolkit.readthedocs.io/en/latest/
* Stack overflow dataset: https://www.kaggle.com/datasets/stackoverflow/stackoverflow?select=posts_answers
* CLERC: https://educationaldatamining.org/files/conferences/EDM2020/papers/paper_64.pdf
* Collaborative filtering: https://towardsdatascience.com/various-implementations-of-collaborative-filtering-100385c6dfe0
* Sentence BERT documentation:https://www.sbert.net/index.html
* Pinecone:https://www.pinecone.io
* Trello: https://trello.com/invite/b/Jhu2emxm/32031292bdcdd27f0875b5006cd378e9/stem-away-virtual-internship
* Micro (minding map of the project): https://miro.com/welcomeonboard/RkM1UFdYaDVTWnROcW5RRGlGYTJLcVd6ODlFb0NheHQ5YzhCQkRPeGJORDJabDY0SnJud1N4cDlkbmMyVTdEVXwzNDU4NzY0NTI4ODcwMzk3ODcz?share_link_id=405538076494

""", unsafe_allow_html=True)


#st.markdown(f'Task 2:')

st.markdown('<h2 style=color:#4169e1;">Prototyping - Web Scraping</h2>', unsafe_allow_html=True)

# st.markdown('<h3 style=color:#4169e1;">Progress Made</h1>', unsafe_allow_html=True)

# st.markdown(""" 
# * Data analysis of sustainability reports.
# * Tabular data successfully extracted using Camelot.
# * Pytesseract was able to extract the text correctly from pages where we have multiple columns in one page, but it did not extract tables/figures.
# * OCR technique worked extremely well and gave a confidence level of 99% in the np array. Extraction was great.
# * ESG bert model has being used to filter sentences with keyword topics and ESG-bert topics.
# * Achieved accuracy for text extraction using EasyOCR is 75% -99%.
# """, unsafe_allow_html=True)

# st.markdown('<h3 style=color:#4169e1;">Next Steps</h1>', unsafe_allow_html=True)

# st.markdown(""" 

# Following are the activities that we need focus on:
# * Ongoing work on text extraction and improvement on the meaningfulness of extracted text.
# * Ongoing work and more focus required on the efficient extraction of chemical formula and symbols. 
# * Improvement in the meaningfulness of extracted text.
# * Multiprocessing of PDF text extraction.
# """, unsafe_allow_html=True)


# #st.markdown(f'Task 3:')

# st.markdown('<h2 style=color:#4169e1;">Task 3 - Modelling</h2>', unsafe_allow_html=True)

# st.markdown('<h3 style=color:#4169e1;">Progress Made</h1>', unsafe_allow_html=True)

# st.markdown(""" 
# * Significant progress has been made in the KPI matching part i.e. connecting sentences with the closest KPIs present in the list provided by Sustain Lab. 
# """, unsafe_allow_html=True)

# st.markdown('<h3 style=color:#4169e1;">Next Steps</h1>', unsafe_allow_html=True)

# st.markdown(""" 

# Following are the activities that we need focus on:

# * The preprocessed datasets and the final KPI list will be passed into the pipeline.
# * Match sentences in the dataset with the KPI using multiple approaches. These may produce different KPI matches. In that case take mode.

# - Fuzzy Name Matching

# - Sentence Embeddings

# - N-gram Embeddings

# * Apply NER based methods to extract values – measurements, date, time, orgs, indicators, etc. Using dependency parsers to match these extracted values to the KPI.
# * We will iteratively improve results by focusing on the problem areas. Some of these we already know :

# - Resolving ambiguous KPIs.

# - Multi-KPIs present in a single sentence.

# - Connecting correct KPIs with their values.

# """, unsafe_allow_html=True)

# st.markdown('<h3 style=color:#4169e1;">References</h1>', unsafe_allow_html=True)

# st.markdown(""" 
#    * https://aaai-kdf2020.github.io/assets/pdfs/kdf2020_paper_24.pdf
#    * https://huggingface.co/nbroad/ESG-BERT
#    * https://towardsdatascience.com/keybert-keyword-extraction-using-bert-a6dc3dd38caf
#    * https://towardsdatascience.com/easy-fine-tuning-of-transformers-for-named-entity-recognition-d72f2b5340e3
#    * https://www.pinecone.io/learn/sentence-embeddings/
# """, unsafe_allow_html=True)


# #st.markdown(f'Task 4:')

# st.markdown('<h2 style=color:#4169e1;">Task 4 - Data Visualizations</h2>', unsafe_allow_html=True)

# st.markdown('<h3 style=color:#4169e1;">Progress Made</h1>', unsafe_allow_html=True)

# st.markdown(""" 
# * Taken key takeaways from the data extracted to bring out the points
# * Created a streamlit app to bring all the works into a single space
# * Showcased all the factors based on the progress done in data collection and data preprocessing
# """, unsafe_allow_html=True)

# st.markdown('<h3 style=color:#4169e1;">Next Steps</h1>', unsafe_allow_html=True)

# st.markdown(""" 

# Following are the activities that we need focus on:
# * Add additional factors along with interactiveness for the upcoming customized data
# * Grab some insights from modelling process to bring clear understanding of the approach that measures the impact
# """, unsafe_allow_html=True)