import os
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain.tools import StructuredTool
from dotenv import load_dotenv

from src.nodes.weather_agent import weather_tool
from src.nodes.poi_agent import poi_tool
from src.nodes.itinerary_creator import itinerary_tool

load_dotenv()

# Define tools
weather = StructuredTool.from_function(
    func=weather_tool,
    name="WeatherTool",
    description="Get weather forecast for a given city and number of days"
)

pois = StructuredTool.from_function(
    func=poi_tool,
    name="POITool",
    description="Get points of interest for a city"
)

itinerary = StructuredTool.from_function(
    func=itinerary_tool,
    name="ItineraryTool",
    description="Create itinerary from POIs and weather"
)

# LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Agent
agent_executor = create_react_agent(llm, [weather, pois, itinerary])

def run_travel_planner(query: str):
    result = agent_executor.invoke({"input": query})
    return result["output"]
