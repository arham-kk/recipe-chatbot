import gradio as gr
import openai

# Set up OpenAI GPT-3.5 credentials
openai.api_key = "OPENAI-API"

def generate_recipe(time_available, num_people, diet_preference, experience_level, ingredients):
    prompt = f"Generate a recipe with the following parameters:\nTime Available: {time_available} minutes\nNumber of People: {num_people}\nDiet Preference: {diet_preference}\nExperience Level: {experience_level}\nAvailable Ingredients: {ingredients}\nRecipe:"
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt,
        max_tokens=500
    )
    recipe = response.choices[0].text.strip()
    return recipe

def generate_with_button(time_available, num_people, diet_preference, experience_level, ingredients):
    if ingredients == "":
        return ""
    recipe = generate_recipe(time_available, num_people, diet_preference, experience_level, ingredients)
    return recipe

inputs = [
    gr.inputs.Slider(minimum=10, maximum=240, step=10, label="Time Available (minutes)"),
    gr.inputs.Number(label="Number of People"),
    gr.inputs.Radio(["Vegan", "Low Calorie", "Regular"], label="Diet Preference"),
    gr.inputs.Radio(["Beginner", "Intermediate", "Advanced"], label="Experience Level"),
    gr.inputs.Textbox(label="Available Ingredients")
]

recipe_generator = gr.Interface(
    fn=generate_with_button,
    inputs=inputs,
    outputs=gr.outputs.Textbox(),
    live=False,
    title="Recipe Generator",
    description="Generate a recipe based on your preferences and available ingredients."
)

recipe_generator.launch()
