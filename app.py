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

print("----Generated Payload----\n")
print(system_prompt)
print("--------------------------\n")


def execute_llm_call(prompt_text, model_engine="gpt-4", **kwargs):
    print(f"Routing request to target model: {model_engine}...")
    print(f"Applying dynamic configuration parameters: {kwargs}")
    print("Awaiting API response...\n")
    return f"Mock API Output: Welcome aboard, {', '.join(active_users)}! Let's get to work."


if __name__ == "__main__":
    api_response = execute_llm_call(
        prompt_text=system_prompt,
        model_engine="gpt-4.1-turbo",
        temperature=0.3,
        top_k=40,
        max_tokens=200
    )

    print(f"Final Result:\n{api_response}")

    
    