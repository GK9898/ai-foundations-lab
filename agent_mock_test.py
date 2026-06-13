import json
import time

users_database = [
    {"id": 101, "name": "Alice", "role": "admin", "is_active": True},
    {"id": 102, "name": "Bob", "role": "user", "is_active": False},
    {"id": 103, "name": "Charlie", "role": "editor", "is_active": True}
]


active_users = [user['name'] for user in users_database if user['is_active']]
print('Active Users are:',active_users)
print(f"Found {len(active_users)} active users.")

context_block = ""

for index, name in enumerate(active_users, start=1):
    context_block += f"{index}. {name}\n"

print(context_block)

system_prompt = f"""
System Instruction: You are a corporate communication assistant.

Task: Write a highly professional welcome message for the following active team members.

Active Members:
{context_block}

Please keep the tone encouraging and brief.
"""

def mock_api_call(payload: dict, simulate_timeout=False, simulate_missing_key=False):
    print("\n--- INITIATING API CALL ---")

    try:
        with open("agent_config.json", "r") as f:
            config = json.load(f)
    except Exception as e:
        print(f"[ERROR] Failed to load config: {e}")
        config = {}

    model_engine = config.get("model_engine", "unknown-model")
    kwargs = {k: v for k, v in config.items() if k != "model_engine"}

    prompt_text = system_prompt
    try:
        #Simulate a missing key error when llm forget to return a mandatory key
        if simulate_missing_key:
            malformed_response = {"text": "Hello, world!"}
            #This line will cause a KeyError because 'usage_metrics' is not in the dictionary
            tokens = malformed_response['usage_metrics']
            print('Tokens used: ', tokens)
        #Simulate a timeout error
        if simulate_timeout:
            #This line will cause a TimeoutError because we are sleeping for 10 seconds
            time.sleep(10)
            raise TimeoutError("The LLM API endpoint took too long to respond.")

        print(f"Routing request to target model: {model_engine}...")
        print(f"Applying dynamic configuration parameters: {kwargs}")
        print("Awaiting API response...\n")
        return f"Mock API Output: Welcome aboard, {', '.join(active_users)}! Let's get to work."

        print("API Call Successful!")
        return True

    except KeyError as e:
        print(f"[CRITICAL ERROR] LLM output parsing failed. Missing expected key: {e}")

    except TimeoutError as e:
        print(f"[NETWORK ERROR] {e} Switching to backup endpoint...")
    # finally always runs
    finally:
        print("API transaction finalized (Connection Closed).")


if __name__ == "__main__":
    #Test 1: Simulate API Timeout
    mock_api_call(payload=active_users, simulate_timeout=True)

    #Test 2: Simulate Missing Key
    mock_api_call(payload=active_users, simulate_missing_key=True)

    #Test 3: Successful API Call using loaded configuration
    response = mock_api_call(payload=active_users)
    print(f"Response: {response}")