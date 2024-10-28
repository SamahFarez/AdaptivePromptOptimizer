# models/llm_chain.py

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load the pre-trained model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def generate_text(prompt, max_new_tokens=100, temperature=0.7, top_k=50, top_p=0.95):
    # Encode the input prompt
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    
    # Generate text
    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=len(input_ids[0]) + max_new_tokens,
            num_return_sequences=1,
            temperature=temperature,  # Controls randomness
            top_k=top_k,              # Limits sampling to top-k words
            top_p=top_p               # Nucleus sampling
        )

    # Decode the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

def initial_chain_invoke(inputs):
    prompt = (
        f"Generate an engaging educational summary in a {inputs['style']} style "
        f"with a {inputs['tone']} tone about {inputs['subject']}."
    )
    return generate_text(prompt)

def refinement_chain_invoke(inputs):
    prompt = (
        f"Based on the feedback '{inputs['feedback']}', refine the following text:\n"
        f"Original: {inputs['initial_content']}"
    )
    return generate_text(prompt)
