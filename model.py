from openai import AzureOpenAI
import json

API_VERSION = "2024-02-01"
MODEL_NAME = "gpt-35-turbo"

def generate_prompt(farm_produce, disease_identified):
    sys_cont = f''' 
        You are a helpful, fun and friendly assistant for farmers.

    Farmers have used the detection app to detect disease in their farm produce.

    In cases where the disease is not clear or the disease identified is an health status like "healthy", then give brief details on how the health status can be mitigated if bad, 
    However if you have clear details about the identified disease from the text below, then just talk about that only and ignore health status. 

    The details of the farm product disease identified is as below:

    Farm produce: {farm_produce} - Disease identified: {disease_identified}

    Give details about the dieases and list steps on how the farmer can mitigate the disease. 
    '''

    MESSAGES = [{"role": "system", "content": sys_cont}]

    return MESSAGES


def load_model():
    ENDPOINT = "https://polite-ground-030dc3103.4.azurestaticapps.net/api/v1"
    API_KEY = "5eb624d1-f6ab-47b5-ab45-e7a316563796"

    API_VERSION = "2024-02-01"
    MODEL_NAME = "gpt-35-turbo"

    client = AzureOpenAI(
        azure_endpoint=ENDPOINT,
        api_key=API_KEY,
        api_version=API_VERSION,
    )
    return client


def generate_q(query, farm_produce, disease_identified):

    sys_cont = f''' 
    You are a helpful, fun and friendly assistant for farmers.

    Farmers have used the detection app to detect disease in their farm produce.

    In cases where the disease is not clear or the disease identified is an health status like "healthy", then give brief details on how the health status can be mitigated if bad, 
    However if you have clear details about the identified disease from the text below, then just talk about that only and ignore health status. 

    The details of the farm product disease identified is as below:

    Farm produce: {farm_produce} - Disease identified: {disease_identified}

    Give details about the dieases and list steps on how the farmer can mitigate the disease. 

    '''

    MESSAGES = [{"role": "system", "content": sys_cont},
    {"role": "user", "content": f"{query}"}]

    return MESSAGES

def get_response(model, messages):
    completion = model.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
        )
    return completion.choices[0].message.content
