from transformers import AutoTokenizer, AutoModelForCausalLM

llama3_model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
token = "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"  # Replace with your token

tokenizer = AutoTokenizer.from_pretrained(llama3_model_id, use_auth_token=token)
model = AutoModelForCausalLM.from_pretrained(llama3_model_id, use_auth_token=token)
