
# Adaptive Prompt Optimizer

This project is an **Adaptive Prompt Optimizer** that generates and refines prompts in an iterative manner. Using text generation models, the optimizer adjusts the initial prompt based on user feedback or set criteria, improving the generated text with each iteration.

## Features
- **Iterative Prompt Refinement**: Based on user feedback, the model refines generated text through iterations.
- **Customizable Prompt Input**: Users can input a prompt directly to shape the generated content.
- **Similarity Scoring**: Uses cosine similarity to measure text closeness and guide prompt adjustments.
- **Auto-feedback Integration**: (optional) Future potential for reinforcement learning to fine-tune prompts dynamically.

## Setup

### Prerequisites
- Python 3.8 or higher
- Git

### Installation
1. **Clone the repository**
    ```bash
    git clone https://github.com/your-username/AdaptivePromptOptimizer.git
    cd AdaptivePromptOptimizer
    ```
2. **Set up a virtual environment** (recommended)
    ```bash
    python3 -m venv apoenv
    source apoenv/bin/activate  # For Unix/Linux
    apoenv\Scripts\activate   # For Windows
    ```
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

### Setting up the Model
By default, the project uses `transformers` for text generation without requiring an OpenAI API key.

## Running the Optimizer
1. **Launch the program**
    ```bash
    python3 main.py
    ```
2. **Input Prompts**: You will be prompted to input an initial prompt. Based on feedback, you can modify prompts to see improved generated text.

### Sample Usage
```plaintext
Initial prompt: "Write an educational summary in a narrative style with an engaging tone about the Industrial Revolution."
Modified prompt after feedback: "Make it more exciting as a story for children"
```

## Future Enhancements
- **Reinforcement Learning Integration**: Implement RL to better refine prompts based on dynamic feedback.
- **Advanced Metrics**: Incorporate additional metrics for quality and relevance scoring.

## Troubleshooting
- If you encounter a `ModuleNotFoundError`, make sure all dependencies in `requirements.txt` are installed.
- For API rate limits or quota issues, use local models as described in the setup.

---

**Enjoy refining your prompts with Adaptive Prompt Optimizer!**
