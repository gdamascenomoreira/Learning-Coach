import os

from dotenv import load_dotenv
from openai import OpenAI
from azure.identity import DefaultAzureCredential
from azure.identity import get_bearer_token_provider

load_dotenv()


def get_response(system_prompt, user_prompt):

    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),
        "https://ai.azure.com/.default"
    )

    client = OpenAI(
        base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=token_provider
    )

    response = client.responses.create(
        model=os.getenv("MODEL_DEPLOYMENT"),
        instructions=system_prompt,
        input=user_prompt
    )

    return response.output_text