from langchain_community.tools.tavily_search import TavilySearchResults
def web_search_tool(question: str) -> str:
    """This tool is useful when we want web search for current events."""
    # Function logic here
    # Step 1: Instantiate the Tavily client with your API key
    websearch = TavilySearchResults()
    # Step 2: Perform a search query
    response = websearch.invoke({"query":question})
    return response