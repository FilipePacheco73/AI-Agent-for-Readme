import json
from datetime import datetime

def log_creation(messages: dict):
    """
    Create a log from a dictionary and save it to a file.
    
    :param messages: The dictionary to be logged.
    """

    # Get the current time for the log
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Initialize token counters
    token_usage = 0
    input_tokens_sum = 0
    output_tokens_sum = 0

    # Temp text to store the log
    temp_log = "\n" + "=" * 50 + "\n"

    for m in messages["messages"]:
        m.pretty_print()
        m_dict = m.dict()
        temp_log += json.dumps(m_dict, indent=2) + "\n"

        if 'response_metadata' in m.__dict__:
            token_usage = m.response_metadata.get('token_usage', {})
            input_tokens_sum += token_usage.get('prompt_tokens', 0)
            output_tokens_sum += token_usage.get('completion_tokens', 0)

    print("\n" + "=" * 50 + "\n")
    print(f"Total input tokens: {input_tokens_sum}")
    print(f"Total output tokens: {output_tokens_sum}")
    print(f"Total tokens: {input_tokens_sum + output_tokens_sum}")

    # Create a log to be saved in a txt file
    log = "=" * 50 + "\n"
    log += f"Log created on: {current_time}\n"
    log += f"Total input tokens: {input_tokens_sum}\n"
    log += f"Total output tokens: {output_tokens_sum}\n"
    log += f"Total tokens: {input_tokens_sum + output_tokens_sum}\n"
    log += temp_log
    log += "End of log\n"
    log += "=" * 50 + "\n"

    # Save the log to a file
    with open(f"src/logs/agent_log_{current_time}.txt", "w") as f:
        f.write(log)