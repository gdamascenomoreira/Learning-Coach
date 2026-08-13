from openai import OpenAI

def get_response(client, model_name, system_prompt, user_prompt):

    response = client.responses.create(
        model=model_name,
        instructions=system_prompt,
        input=user_prompt
    )

    return response.output_text
