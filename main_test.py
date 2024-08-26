from crewai import Crew, Agent, Task
from agents.routeragent import router_tool
from agents.retriveragent import retriver_tool
from langchain_groq import ChatGroq
import pydantic
import os 

import os
os.environ['GROQ_API_KEY'] = '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'
# Setup the LLM
llm = ChatGroq(
    model_name="llama-3.1-70b-versatile",
    temperature=0.1,
    max_tokens=1000,
)

# Setup the Router Agent
Router_Agent = Agent(
    role='Router',
    goal='Route user question to a text to image or text to speech or web search',
    backstory=(
        "You are an expert at routing a user question to a text to image or text to speech or web search."
        "Use the text to image to generate images from textual descriptions."
        "Use the text to speech to convert text to speech."
        "Use the image to text to generate text describing the image based on the textual description."
        "Use the web search to search for current events."
        "You do not need to be stringent with the keywords in the question related to these topics. Otherwise, use web-search."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[router_tool],
)

# Setup the Retriever Agent
Retriever_Agent = Agent(
    role="Retriever",
    goal="Use the information retrieved from the Router to answer the question and image url provided.",
    backstory=(
        "You are an assistant for directing tasks to respective agents based on the response from the Router."
        "Use the information from the Router to perform the respective task."
        "Do not provide any other explanation"
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[retriver_tool],
)

# Setup the Router Task
router_task = Task(
    description=(
        "Analyse the keywords in the question {question}"
        "If the question {question} instructs to describe a image then use the image url {image_url} to generate a detailed and high quality images covering all the nuances described in the textual descriptions provided in the question {question}."
        "Based on the keywords decide whether it is eligible for a text to image or text to speech or web search."
        "Return a single word 'text2image' if it is eligible for generating images from textual description."
        "Return a single word 'text2speech' if it is eligible for converting text to speech."
        "Return a single word 'image2text' if it is eligible for describing the image based on the question {question} and image url {image_url}."
        "Return a single word 'web_search' if it is eligible for web search."
        "Do not provide any other preamble or explanation."
    ),
    expected_output=(
        "Give a choice 'web_search' or 'text2image' or 'text2speech' or 'image2text' based on the question {question} and image url {image_url}"
        "Do not provide any preamble or explanations except for 'text2image' or 'text2speech' or 'web_search' or 'image2text'."
    ),
    agent=Router_Agent,
)

# Setup the Retriever Task
retriever_task = Task(
    description=(
        "Based on the response from the 'router_task' generate response for the question {question} with the help of the respective tool."
        "Use the web_search_tool to retrieve information from the web in case the router task output is 'web_search'."
        "Use the text2speech tool to convert the text to speech in English in case the router task output is 'text2speech'."
        "Use the text2image tool to convert the text to speech in English in case the router task output is 'text2image'."
        "Use the image2text tool to describe the image provided in the image URL in case the router task output is 'image2text'."
    ),
    expected_output=(
        "You should analyze the output of the 'router_task'"
        "If the response is 'web_search' then use the web_search_tool to retrieve information from the web."
        "If the response is 'text2image' then use the text2image tool to generate a detailed and high quality image covering all the nuances described in the textual descriptions provided in the question {question}."
        "If the response is 'text2speech' then use the text2speech tool to convert the text to speech."
        "If the response is 'image2text' then use the image2text tool to describe the image based on the textual description."
    ),
    agent=Retriever_Agent,
    context=[router_task],

)

from crewai import Crew,Process
crew = Crew(
    agents=[Router_Agent,Retriever_Agent],
    tasks=[router_task,retriever_task],
    verbose=True,
)

inputs ={"question":"Generate an image based upon this text: a close up portfolio photo of a beautiful Indian Model woman, perfect eyes, bright studio lights, bokeh, 50mm photo, neon pink visor","image_url":" "}
result = crew.kickoff(inputs=inputs)
result.raw
inputs ={"question":"Provide a detailed description.","image_url":"https://images.unsplash.com/photo-1470770903676-69b98201ea1c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80.jpg"}
result = crew.kickoff(inputs=inputs)
result.raw
inputs_speech ={"question":"Generate a speech for this text: The image features a small white dog running down a dirt path.The dog is happily smiling as it runs and the path is lined with beautiful blue flowers.","image_url":" "}
result = crew.kickoff(inputs=inputs_speech)
result.raw
inputs = {"question":"tourist destinations in India.","image_url":" "}
result = crew.kickoff(inputs=inputs)
result.raw
