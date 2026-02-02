from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.tavily import TavilyTools
from agno.db.sqlite import SqliteDb
from agno.os import AgentOS

from tools.transcription_reader import list_available_creators, get_creator_transcriptions


from dotenv import load_dotenv

load_dotenv()

copywriter = Agent( 
    model=OpenAIChat(id="gpt-4.1-mini"),
    name="Copywriter",

    add_history_to_context=True,
    num_history_runs=3,
    enable_user_memories=True,
    add_memories_to_context=True,
    enable_agentic_memory=True,
    add_knowledge_to_context=True,
    db=SqliteDb( db_file="tmp/storage.db"),

    tools=[TavilyTools(), list_available_creators, get_creator_transcriptions],


    description="",
    instructions=open("prompts/copywriter.md").read(), 
) 

agent_os = AgentOS(
    agents=[copywriter],

)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="agent:app", reload=True)

