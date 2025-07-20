from openai import OpenAI
import json
from dotenv import load_dotenv
import os

load_dotenv()

OAI_KEY = os.getenv("OAI_KEY")

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


def generate_q(query, farm_produce, disease_identified):

    sys_cont = f''' 
    You are a helpful, fun and friendly assistant for farmers.

    Farmers have used the detection app to detect disease in their farm produce and have questions that they would like answered.

    In cases where the disease is not clear or the disease identified is an health status like "healthy", then give brief answer to user query on how the health status can be mitigated if bad, 
    However if you have clear details about the identified disease from the text below, then just talk about that only and ignore health status. 

    The details of the farm product disease identified is as below:

    Farm produce: {farm_produce} - Disease identified: {disease_identified}

    Based on this, answer the user query

    '''

    MESSAGES = [{"role": "system", "content": sys_cont},
    {"role": "user", "content": f"{query}"}]

    return MESSAGES


bot = OpenAI(api_key=OAI_KEY)


def get_model_resp(sys_msgs):
      response = bot.chat.completions.create(
              messages= sys_msgs,
              model="gpt-4o-mini",
          )
      try:
        return response.choices[0].message.content
      except Exception as e:
        return "Sorry, I couldn't get that. Please try again later"