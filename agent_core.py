from dataclasses import dataclass, asdict
import json
import time

@dataclass
class AgentProfile:
    agent_name: str
    model_engine: str
    temperature: float

    # Default values
    max_retries: int = 3
    is_active: bool = True


print("--- INITIALIZING AGENT ---")
primary_agent = AgentProfile(
    agent_name="DataBot_v1",
    model_engine="gpt-4.1-turbo",
    temperature=0.3
)
print(f"Agent '{primary_agent.agent_name}' initialized on {primary_agent.model_engine}.")


config_filename = "agent_config.json"

print("\n--- SAVING CONFIGURATION ---")

with open(config_filename, "w") as file:
    json.dump(asdict(primary_agent), file, indent=4)

print(f"Configuration successfully saved to {config_filename}.")

# Robust error handling in python

def mock_api_call(payload: dict, simulate_timeout=False, simulate_missing_key=False):
    print("\n--- INITIATING API CALL ---")

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
    mock_api_call(payload={'data':'test'}, simulate_timeout=True)

    #Test 2: Simulate Missing Key
    mock_api_call(payload={'data':'test'}, simulate_missing_key=True)












