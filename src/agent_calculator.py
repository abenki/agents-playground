from smolagents import tool, CodeAgent, HfApiModel
from dotenv import load_dotenv
import os
import yaml

load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")


@tool
def add(a: float, b: float) -> float:
    """Add two numbers.
    Args:
        a: a float representing the first number
        b: a float representing the second number
    """
    return a + b


@tool
def multiply(a: float, b: float) -> float:
    """Multiply two integers.
    Args:
        a: a float representing the first number
        b: a float representing the second number
    """
    return a * b


@tool
def subtract(a: float, b: float) -> float:
    """Subtract two integers.
    Args:
        a: a float representing the first number
        b: a float representing the second number
    """
    return a - b


@tool
def divide(a: float, b: float) -> float:
    """Divide two integers.
    Args:
        a: a float representing the first number
        b: a float representing the second number
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

model = HfApiModel(
    max_tokens=2096,
    temperature=0.5,
    model_id='Qwen/Qwen2.5-Coder-32B-Instruct',
    custom_role_conversions=None,
    token=HF_API_KEY,
)

with open("/Users/anass/Developer/agents-playground/prompts.yaml", 'r') as stream:
    prompt_templates = yaml.safe_load(stream)
    
# We're creating our CodeAgent
agent = CodeAgent(
    model=model,
    tools=[add, subtract, multiply, divide], # add your tools here (don't remove final_answer)
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    prompt_templates=prompt_templates,
)

agent.run(
    "I have 3 apples. Marcus takes 2 of them, Janice gives me 4. Then, Daniel doubles the amount of apples I have. How many apples do I have in the end?"
)
