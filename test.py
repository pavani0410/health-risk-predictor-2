from transformers import AutoTokenizer, AutoModelForCausalLM
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

llama3_model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
token = os.getenv('HUGGINGFACE_TOKEN')  # Get token from environment variable

if not token:
    raise ValueError("HUGGINGFACE_TOKEN environment variable is not set")

tokenizer = AutoTokenizer.from_pretrained(llama3_model_id, use_auth_token=token)
model = AutoModelForCausalLM.from_pretrained(llama3_model_id, use_auth_token=token)
