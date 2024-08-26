import streamlit as st
from crewai import Crew, Agent, Task
from agents.routeragent import router_tool
from agents.retriveragent import retriver_tool
from langchain_groq import ChatGroq
import json

# Set up the environment variable for the API key
import os
os.environ['GROQ_API_KEY'] = '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'

# Set up the LLM
llm = ChatGroq(
    model_name="llama-3.1-70b-versatile",
    temperature=0.1,
    max_tokens=1000,
)

# Set up the Router Agent
Router_Agent = Agent(
    role='Router',
    goal='Route user question to a text to image or text to speech or web search',
    backstory=(
        "You are an expert at routing a user question to a text to image or text to speech or web search."
        "Use the text to image to generate images from textual descriptions."
        "Use the text to speech to convert text to speech."
        "Use the image to text to generate text describing the image based on the textual description."
        "Use the web search to search for current events."
        "You do not need to be stringent with the keywords in the question related to these topics. Otherwise, use web search."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[router_tool],
)

# Set up the Retriever Agent
Retriever_Agent = Agent(
    role="Retriever",
    goal="Use the information retrieved from the Router to answer the question and image URL provided.",
    backstory=(
        "You are an assistant for directing tasks to respective agents based on the response from the Router."
        "Use the information from the Router to perform the respective task."
        "Do not provide any other explanation."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[retriver_tool],
)

# Set up the Router Task
router_task = Task(
    description=(
        "Analyze the keywords in the question {question}. "
        "If the question {question} instructs to describe an image, then use the image URL {image_url} to generate a detailed and high-quality image covering all the nuances described in the textual descriptions provided in the question {question}. "
        "Based on the keywords, decide whether it is eligible for text to image, text to speech, or web search. "
        "Return a single word 'text2image' if it is eligible for generating images from textual descriptions. "
        "Return a single word 'text2speech' if it is eligible for converting text to speech. "
        "Return a single word 'image2text' if it is eligible for describing the image based on the question {question} and image URL {image_url}. "
        "Return a single word 'web_search' if it is eligible for web search."
    ),
    expected_output=(
        "Give a choice: 'web_search', 'text2image', 'text2speech', or 'image2text' based on the question {question} and image URL {image_url}. "
        "Do not provide any preamble or explanations except for 'text2image', 'text2speech', 'web_search', or 'image2text'."
    ),
    agent=Router_Agent,
)

# Set up the Retriever Task
retriever_task = Task(
    description=(
        "Based on the response from the 'router_task', generate a response for the question {question} with the help of the respective tool. "
        "Use the web_search_tool to retrieve information from the web if the router task output is 'web_search'. "
        "Use the text2speech tool to convert the text to speech in English if the router task output is 'text2speech'. "
        "Use the text2image tool to generate a detailed and high-quality image covering all the nuances described in the textual descriptions provided in the question {question} if the router task output is 'text2image'. "
        "Use the image2text tool to describe the image provided in the image URL if the router task output is 'image2text'."
    ),
    expected_output=(
        "You should analyze the output of the 'router_task'. "
        "If the response is 'web_search', then use the web_search_tool to retrieve information from the web. "
        "If the response is 'text2image', then use the text2image tool to generate a detailed and high-quality image covering all the nuances described in the textual descriptions provided in the question {question}. "
        "If the response is 'text2speech', then use the text2speech tool to convert the text to speech. "
        "If the response is 'image2text', then use the image2text tool to describe the image based on the textual description."
    ),
    agent=Retriever_Agent,
    context=[router_task],
)

# Initialize the Crew
crew = Crew(
    agents=[Router_Agent, Retriever_Agent],
    tasks=[router_task, retriever_task],
    verbose=True,
)

# Streamlit app layout
st.title("AI-Powered Multimedia Assistant")

# Image generation input
st.subheader("Generate an Image")
question_t2i = st.text_input("Enter a textual description for image generation:")
if st.button("Generate Image"):
    inputs = {"question": question_t2i, "image_url": ""}
    result = crew.kickoff(inputs=inputs)
    st.write(result.raw)  # Log the raw result to understand its structure
    
    # Assuming result.raw contains the image URL directly or in a JSON structure
    try:
        if isinstance(result.raw, str):
            st.image(result.raw)
        else:
            result_data = json.loads(result.raw)
            st.image(result_data['image_url'])
    except Exception as e:
        st.error(f"Error displaying image: {e}")

# Text to speech input
st.subheader("Convert Text to Speech")
question_t2s = st.text_input("Enter text to convert to speech:")
if st.button("Convert Text to Speech"):
    inputs_speech = {"question": question_t2s, "image_url": ""}
    result = crew.kickoff(inputs=inputs_speech)
    st.write(result.raw)  # Log the raw result to understand its structure
    
    # Assuming result.raw contains a URL to the audio file or base64 encoded audio
    try:
        if isinstance(result.raw, str):
            st.audio(result.raw)
        else:
            result_data = json.loads(result.raw)
            st.audio(result_data['audio_url'])
    except Exception as e:
        st.error(f"Error playing audio: {e}")

# Web search input
st.subheader("Web Search")
question_ws = st.text_input("Enter a query for web search:")
if st.button("Perform Web Search"):
    inputs_ws = {"question": question_ws, "image_url": ""}
    result = crew.kickoff(inputs=inputs_ws)
    st.write(result.raw)  # Log the raw result to understand its structure
    
    # Assuming result.raw contains the search results
    try:
        if isinstance(result.raw, str):
            st.write(result.raw)
        else:
            result_data = json.loads(result.raw)
            st.write(result_data['search_results'])
    except Exception as e:
        st.error(f"Error displaying web search results: {e}")

# Image to text input
st.subheader("Describe an Image")
image_url = st.text_input("Enter an image URL for description:")
if st.button("Describe Image"):
    inputs = {"question": "Provide a detailed description.", "image_url": image_url}
    result = crew.kickoff(inputs=inputs)
    st.write(result.raw)  # Log the raw result to understand its structure
    
    # Assuming result.raw contains the description text
    try:
        if isinstance(result.raw, str):
            st.write(result.raw)
        else:
            result_data = json.loads(result.raw)
            st.write(result_data['description'])
    except Exception as e:
        st.error(f"Error displaying image description: {e}")
