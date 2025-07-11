def get_aifred_response(messages):
    # This is a placeholder function. It simulates the AI's response.
    # It allows me to test the entire app flow without using a real LLM yet.
    print("[LLM Service: MOCK RESPONSE]")
    last_user_message = messages[-1]["content"]
    mock_response = f"I have recieved your message: '{last_user_message}'. The system is responding correctly."
    return mock_response