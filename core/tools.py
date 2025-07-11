def get_weather(location):
    return f"The weather in {location} is clear."

def reboot_server(server_ip):
    # WARNING: This is a dangerous, priveleged function.
    # ... logic to send a reboot command ...
    return f"Reboot command sent to server {server_ip}."

# Alfred's standard toolkit
AGENT_TOOLS = {
    "get_weather": get_weather
    # "Play_music", "control_lights", etc.
}

# The Administrator's toolkit
ORACLE_TOOLS = {
    # Includes all agent tools
    **AGENT_TOOLS,
    # ...plus the dangerous ones
    "reboot_server": reboot_server
    # "run_kali_scan", "access_evidence_locker", etc.
}