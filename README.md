# Recipe Suggestions Chatbot

This project utilizes OpenAI's text generation model to suggest recipes based on a list of ingredients & prefrences provided by the user.


https://github.com/arham-kk/recipe-chatbot/assets/108623726/98e19fd0-39df-428d-afff-968e665b2888


## How it Works

1. The user inputs time available (minutes), number of people, experience level, diet preference and list of available ingredients (comma-separated) into the provided textbox.
2. The system generates custom prompts using the provided ingredients.
3. OpenAI's text generation model generates recipe suggestions based on the prompts.
4. The suggested recipes are displayed in the output textbox.

## Usage

1. Install the required dependencies by running the following command --> `pip install gradio openai`
2. Set up your OpenAI API credentials by replacing `YOUR_API_KEY` with your actual API key in the code
3. Run the application by executing the following command --> `python.app`
4. Access the application by opening the provided URL in your web browser.
