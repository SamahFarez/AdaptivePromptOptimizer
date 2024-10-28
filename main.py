import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load models
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
embedder = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # For feedback similarity

model.eval()

def generate_text(prompt, max_length=100, temperature=0.7):
    # Generate text with repetition penalty
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(
        inputs['input_ids'],
        max_length=max_length,
        temperature=temperature,
        no_repeat_ngram_size=3,
        pad_token_id=tokenizer.eos_token_id,
        attention_mask=inputs['attention_mask']
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)

def score_feedback(refined_text, initial_text):
    # Score the refinement based on cosine similarity
    embeddings = embedder.encode([refined_text, initial_text])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])
    return similarity[0][0]  # Returns a similarity score between 0 and 1

def interactive_prompt_optimizer(initial_prompt, max_iterations=3):
    prompt = initial_prompt
    print(f"Initial prompt: {prompt}")

    for iteration in range(max_iterations):
        print(f"\n== Iteration {iteration + 1} ==")
        
        # Generate text
        output = generate_text(prompt, max_length=150)
        print(f"\nGenerated Text:\n{output}\n")
        
        # Gather feedback
        print("Enter a new prompt or feedback to refine the text, or type 'exit' to finish.")
        feedback = input("New prompt/Feedback: ")
        
        if feedback.lower() == 'exit':
            print("Exiting prompt refinement.")
            break
        
        # Score the generated text for quality improvement
        similarity_score = score_feedback(output, initial_prompt)
        if similarity_score > 0.8:
            print("Feedback is too similar; try more distinct feedback.")
        else:
            # Create new prompt based on feedback
            prompt = f"{initial_prompt} ({feedback})"

    return output

# Example Usage
initial_prompt = "Write an educational summary in a narrative style with an engaging tone about the Industrial Revolution."
final_output = interactive_prompt_optimizer(initial_prompt)

print(f"\n== Final Output ==\n{final_output}")
