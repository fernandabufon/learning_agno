'''
This code is from the  Guide for the Agno Framework.
You can find the guide here: https://docs.agno.com/agents/building-agents
'''

from agno.agent import Agent # Primary class for creating agents
from agno.models.openai import OpenAIResponses
from agno.tools.hackernews import HackerNewsTools # Tools for interacting with Hacker News

agent = Agent( # Create an agent instance
    name="Agno Assist", # Name
    model=OpenAIResponses(id="gpt-5-nano"), # LLM model
    tools=[HackerNewsTools()],  # Tools for interacting with Hacker News
    # More tools at https://docs.agno.com/tools/toolkits/overview
    instructions="Write a report on the topic. Output only the report.",                          # last 3 conversations
    markdown=True, # enable markdown formatting in responses
)

# Use Agent.print_response() for development. It prints the response in a readable format in your terminal.
agent.print_response("Trending startups and products.", stream=True) # User message
# For production, use Agent.run() or Agent.arun():
