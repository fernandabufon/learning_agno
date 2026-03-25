from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.tools.file import FileTools
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


os.getenv("OPENAI_API_KEY")
# Ou os.environ.get("OPENAI_API_KEY") - dá na mesma, mas o getenv é mais comum para variáveis de ambiente.

'''
Reads the job listing and extracts the most important requirements,
responsibilities, and keywords that the employer is looking for.
'''

parent_path = Path(__file__).parent.parent
data_path = Path(__file__).parent.parent / "data"


agent = Agent(
    model=OpenAIResponses(id="gpt-5-nano-2025-08-07", reasoning_effort="low"),
    tools=[FileTools(base_dir=data_path)],
    instructions="Read the job listing and extract the most important requirements, responsibilities, and keywords that the employer is looking for. Create a file that summarizes the key points and most important requirements of the job with the name of job_summary.txt. The summary must be concise and small - containing only the key requirements for the opportunity.",
)

#É importante salvar os logs
# Próximo passo: encapsular o agente em um objeto para utilizar em outros códigos.
output = agent.run("Read the job listing in the job.txt file.")

print(output.content)