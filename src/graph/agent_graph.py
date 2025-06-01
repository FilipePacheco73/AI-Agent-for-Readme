from langgraph.graph import MessagesState, START, END, StateGraph
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_openai import ChatOpenAI
from tools.tool_util import list_repo_contents, read_content


def configure_llm_with_tools(model_name: str) -> tuple:
    """
    Configures the LLM model with the required tools.
    Args:
        model_name (str): The name of the LLM model to be used.
    Returns:
        tuple: A tuple containing the configured LLM model and the list of tools.
    """
    tools = [list_repo_contents, read_content]
    llm = ChatOpenAI(model_name=model_name).bind_tools(tools)
    return llm, tools


def create_base_agent(llm) -> callable:
    def base_agent(state: MessagesState) -> dict:
        """
        Base agent function that processes messages and invokes tools if necessary.
        Args:
            state (MessagesState): The current state of the messages.
        Returns:
            dict: A dictionary containing the processed messages.
        """
        return {"messages": [llm.invoke(state["messages"])]}
    return base_agent


def build_agent_graph(base_agent_fn, tools) -> StateGraph:
    """
    Builds the state graph for the main agent.
    Args:
        base_agent_fn (function): The base agent function to be used in the graph.
        tools (list): A list of tools that can be invoked by the agent.
    Returns:
        StateGraph: The compiled state graph agent ready for invocation.
    """
    builder = StateGraph(MessagesState)

    builder.add_node("base_agent", base_agent_fn)
    builder.add_node("tools", ToolNode(tools))

    builder.add_edge(START, "base_agent")
    builder.add_conditional_edges("base_agent", tools_condition)
    builder.add_edge("tools", "base_agent")

    graph = builder.compile()
    graph.get_graph().draw_mermaid_png(output_file_path='src/graph/main_agent_graph.png')
    return graph


def main_agent(model_name: str = 'gpt-4o-mini') -> StateGraph:
    """
    Creates a state graph agent that interacts with tools to gather information about a GitHub repository.
    This agent uses a base agent function to process messages and a set of tools to gather repository contents.
    The agent is designed to be flexible and can be extended with additional tools as needed.
    Returns:
        StateGraph: The compiled state graph agent ready for invocation.
    """
    llm, tools = configure_llm_with_tools(model_name)
    base_agent_fn = create_base_agent(llm)
    return build_agent_graph(base_agent_fn, tools)