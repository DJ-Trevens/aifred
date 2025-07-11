from multiprocessing import AuthenticationError
from core.persona import AIFRED_BASE_PROMPT, AGENT_CONSTRAINTS, ORACLE_OVERRIDE_PROMPT, get_user_profile
from core.llm_service import get_aifred_response
from core.tools import AGENT_TOOLS, ORACLE_TOOLS

CURRENT_VERSION = "0.1"
PROTOCOL_NAME = "Mockingbird"

current_access_level = "AGENT"
current_system_prompt = AIFRED_BASE_PROMPT + AGENT_CONSTRAINTS

def run_aifred():
    # Load user profile and create the final system prompt
    user = get_user_profile()
    final_system_prompt = current_system_prompt + f"\n\nOperational Notes: The current user's honorific is '{user['honorific']}'."
    messages = [{'role': 'system', 'content': final_system_prompt}]

    print(f"--- A.I.F.R.E.D. v{CURRENT_VERSION} ({PROTOCOL_NAME} Protocol Online) ---")
    print("System configured for user: {user['name']}")
    print("Enter 'exit' to end session.")

    while True:
        user_input = input(f"{user['name'].capitalize()}: ")
        if user_input.lower() == "exit":
            print("Alfred: Goodbye, user['honorific'].")
            break
        
        if current_access_level == "ORACLE":
            system_prompt = AIFRED_BASE_PROMPT + ORACLE_OVERRIDE_PROMPT
        else:
            system_prompt = AIFRED_BASE_PROMPT + AGENT_CONSTRAINTS
        messages.append({'role': 'user', 'content': user_input})

        # Call our MOCK function
        aifred_response = get_aifred_response(messages)

        print(f"Alfred: {aifred_response}")
        messages.append({'role': 'assistant', 'content': aifred_response})

def use_tool(tool_name, tool_params, access_level):
    if access_level == "ORACLE":
        tool_set = ORACLE_TOOLS
    else:
        tool_set = AGENT_TOOLS
    
    if tool_name in tool_set:
        function_to_call = tool_set[tool_name]
        # Safely call the function with its parameters
        return function_to_call(**tool_params)
    else:
        return f"Error: the tool '{tool_name}' is not available at your current access level."

def authenticate_and_elevate():
    global current_access_level
    # ... logic for Yubikey challenge-response ...
    authentication_successful = True
    if authentication_successful:
        current_access_level = "ORACLE"
        print("[System: Oracle Level Access Granted]")
        return True
    return False

def revert_elevated_access():
    global current_access_level
    current_access_level = "AGENT"
    print("[System: Revetred to Agent Level Access]")

def handle_user_input(user_input):
    global current_access_level
    if current_access_level == "AGENT":
        if user_input.lower() == "elevate":
            return authenticate_and_elevate()
if __name__ == "__main__":
    run_aifred()
