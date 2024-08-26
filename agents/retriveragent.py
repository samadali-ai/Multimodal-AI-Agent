from tools.websearch_tool import web_search_tool
from tools.text2speech_tool import text2speech
from tools.text2image_tool import text2image
from tools.image2text_tool import image2text
from langchain_groq import ChatGroq
from crewai_tools import tool

llm = ChatGroq(model_name="llama-3.1-70b-versatile",
    temperature=0.1,
    max_tokens=1000,
)
@tool("retriver tool")
def retriver_tool(router_response: str, question: str, image_url: str) -> str:
    """Retriever Function"""
    #if router_response == 'text2image':
        #return text2image(question)
    if router_response == 'text2speech':
        return text2speech(question)
    #elif router_response == 'image2text':
    #   return image2text(image_url, question)
    else:
        return web_search_tool(question)
