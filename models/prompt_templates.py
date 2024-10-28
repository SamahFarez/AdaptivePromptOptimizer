# models/prompt_templates.py
from langchain.prompts import PromptTemplate

# Initial content prompt template
initial_prompt_template = PromptTemplate(
    input_variables=["intent", "style", "tone", "subject"],
    template="Write a {intent} piece in a {style} style and {tone} tone about {subject}."
)

# Refinement prompt template that incorporates user feedback
refinement_prompt_template = PromptTemplate(
    input_variables=["intent", "style", "tone", "subject", "feedback"],
    template="Rewrite the content with a {intent} approach in a {style} style, {tone} tone about {subject}. "
             "Ensure it is {feedback}."
)
