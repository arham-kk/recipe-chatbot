import gradio as gr
import openai

# Set up your OpenAI API credentials
openai.api_key = "OPENAI-API"

# Define the OpenAI engine
ENGINE_NAME = "text-davinci-003"

# Define the function for generating recipes
def generate_recipes(ingredients):
    custom_prompt = "You have the following ingredients: " + ", ".join(ingredients) + "\n"
    prompt = f"{custom_prompt}Please suggest some recipes using these ingredients.\n"

    response = openai.Completion.create(engine=ENGINE_NAME, prompt=prompt, max_tokens=1000, temperature=0.5, top_p=1.0, n=5, stop=None, timeout=10)
    recipes = [choice.text.strip() for choice in response.choices]
    return recipes

# Create a Gradio interface
def recipe_suggestion(ingredients):
    recipes = generate_recipes(ingredients)
    recipe_list = "\n\n".join([f"Recipe {i + 1}:\n{recipe}" for i, recipe in enumerate(recipes)])
    return recipe_list

inputs = gr.inputs.Textbox(label="List of Ingredients (comma-separated)")
output = gr.outputs.Textbox(label="Recipe Suggestions")

gr.Interface(fn=recipe_suggestion, inputs=inputs, outputs=output, title="Recipe Suggestions", height=400, width=800).launch()
