
```markdown
🍽️ LLM-Powered Restaurant Idea Generator:

<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain" /> <img src="https://img.shields.io/badge/Groq-f37021?style=for-the-badge" alt="Groq" /> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" /> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />

An AI-driven web application that dynamically generates catchy restaurant names and tailored food menus based on a user's selected culinary style. 

Built to demonstrate the orchestration capabilities of **LangChain** combined with Large Language Models and **Streamlit**, this project serves as a practical implementation of LLM chaining, prompt engineering, and rapid web UI development.

🚀 Features:

* Dynamic Text Generation:** Leverages LLMs to creatively brainstorm restaurant names and generate matching, comma-separated menu items.
* Advanced LLM Orchestration:** Utilizes LangChain's `SequentialChain` to link multiple prompts together. The output of the first prompt (the restaurant name) is seamlessly passed as the input to the second prompt (the menu generator).
* Interactive Web Interface:** Features a clean, user-friendly frontend built with Streamlit, allowing users to select cuisines (e.g., Mexican, Indian, Italian, Arabic) from a sidebar dropdown.
* Secure Key Management:** Implements best practices for API key security by abstracting credentials away from the main application code.

🛠️ Tech Stack:

* Core Framework: LangChain (https://python.langchain.com/) - Used to build and manage the LLM application architecture.
* LLM Provider: Groq (https://groq.com/) and OpenAI (https://openai.com/) - Powers the creative reasoning engine behind the text generation.
* Frontend: Streamlit (https://streamlit.io/) - Used for rapid proof-of-concept deployment, entirely in Python, bypassing the need for complex frontend frameworks like React.
* Language: Python.

🧠 How It Works (The Architecture):

This application breaks away from standard single-prompt LLM calls by utilizing *Sequential Chains*. 

1. Prompt Template 1 (Name Generation): The user selects a `cuisine` via the Streamlit sidebar. This variable is passed into the first LangChain Prompt Template to ask the LLM for a fancy restaurant name.
2. Prompt Template 2 (Menu Generation): The output from the first chain (the newly generated restaurant name) acts as the input variable for the second chain, which asks the LLM to output a list of relevant menu items.
3. Sequential Execution: LangChain executes these sequentially, outputting a consolidated dictionary containing both the `restaurant_name` and `menu_items`.
4. UI Rendering: Streamlit strips trailing whitespace, splits the comma-separated string of menu items into a list, and renders them cleanly on the page.

⚙️ Installation & Setup:

Follow these steps to run the project locally.

1. Clone the Repository
```bash
git clone https://github.com/YourUsername/restaurant-idea-generator.git
cd restaurant-idea-generator
```

2. Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install langchain streamlit
```
*(Note: Be sure to also install the specific SDK for your chosen LLM provider, such as openai or langchain-groq.)*

3. Set Up Your API Key
To interact with the language models, you need to provide your API key.
1. Create a file named `secret_key.py` in the root directory and add your key:
```python
# secret_key.py
api_key = "your-unique-api-key-here"
```
*(Make sure to add secret_key.py to your .gitignore file to prevent exposing your credentials publicly.)*

4. Run the Application
Launch the Streamlit server from your terminal:
```bash
streamlit run main.py
```
The application will automatically open in your default web browser.

💡 Usage:

1. Open the web app.
2. Navigate to the sidebar on the left side of the screen and locate the "Pick a Cuisine" dropdown.
3. Select your desired culinary style (e.g., American, Mexican, Arabic).
4. Watch as the application generates a unique restaurant name as a main header, followed by a dynamically generated list of delicious menu items!

## 🤝 Acknowledgements
* This project was inspired by the *LangChain Course For Beginners* by codebasics. 
```
