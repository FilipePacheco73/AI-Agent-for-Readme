from langchain_core.messages import HumanMessage, SystemMessage

# System Message
def system_message() -> SystemMessage:
    return SystemMessage(
        content="""You are a helpful assistant and your main goal is to build a Readme.MD file for a GitHub repository based on the user's input and the information you gather. 
        You can also execute tools to gather information when necessary.
        """
    )

# Human Message
def human_message(user_input: str) -> HumanMessage:
    return HumanMessage(
        content=user_input
    )