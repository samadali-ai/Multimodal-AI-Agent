from crewai_tools import tool
import os
os.environ['GROQ_API_KEY'] = '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'
from langchain_groq import ChatGroq
llm = ChatGroq(model_name="llama-3.1-70b-versatile",
    temperature=0.1,
    max_tokens=1000,
)
## Router Tool
@tool("router tool")
def router_tool(question:str) -> str:
  """Router Function"""
  prompt = f"""Based on the Question provide below determine the following:
1. Is the question directed at generating image ?
2. Is the question directed at describing the image ?
3. Is the question directed at converting text to speech?.
4. Is the question a generic one and needs to be answered searching the web?
Question: {question}

RESPONSE INSTRUCTIONS:
- Answer either 1 or 2 or 3 or 4.
- Answer should strictly be a string.
- Do not provide any preamble or explanations except for 1 or 2 or 3 or 4.

OUTPUT FORMAT:
1
"""
  response = llm.invoke(prompt).content
  if response == "1":
    return 'text2image'
  elif response == "3":
    return 'text2speech'
  elif response == "4":
    return 'web_search'
  else:
    return 'image2text'