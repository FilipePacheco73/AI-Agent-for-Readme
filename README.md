# 📖 AI-Agent-for-Readme

This repository hosts the code for an AI Agent designed to automatically create detailed README files for GitHub repositories. Leveraging a collection of automated tools and machine learning capabilities, it analyzes repository contents and generates a comprehensive README file formatted in Markdown.

## ✨ Features

- Automated README generation with detailed project information.
- Utilizes AI to understand and interpret repository contents.
- Fetches repository structure, commits, contributors, and more.
- Generates an interactive flow chart depicting module interactions.
- Supports a wide range of programming languages through analysis tools.

## 🚀 Installation

To set up this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/FilipePacheco73/AI-Agent-for-Readme.git
   cd AI-Agent-for-Readme
   ```

2. **Install the required Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables for authentication:**
   - OpenAI API key
   - GitHub token

4. **Run the agent:**
   ```bash
   python src/agent_execution/main.py
   ```

## 🛠️ Usage

To use the AI Agent, provide it with a GitHub repository URL. The agent will analyze the repository's contents and generate a README file automatically.

```python
# Example
user_input = 'Can you create a Readme file for this repo https://github.com/FilipePacheco73/AI-Agent-for-Readme?'
```

## 📦 Technologies

- **Programming Language:** Python
- **Frameworks & Libraries:**
  - Langchain
  - Langgraph
  - OpenAI

## 🔧 Configuration

Environment variables are critical for the operation of this AI agent:

- **OPENAI_API_KEY:** Required to interact with OpenAI models.
- **GITHUB_TOKEN:** Required for accessing private GitHub repositories.

## ✅ Requirements

- Python 3.8 or later
- Access to OpenAI API

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add feature - your feature name'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request with a detailed description of your changes.

## 📄 Documentation

Refer to the files within the `docs` directory for more detailed information.

## ❤️ Acknowledgements

Thanks to the contributors who have helped in developing this project.

- **Filipe Pacheco:** Main developer and maintainer.

## 📝 Changelog

- **Update changelog description to clarify its purpose** (June 1, 2025)
- **Enhanced README generation** (June 1, 2025)
- **Improved logging and structured tests** (June 1, 2025)
- **Initial code base setup** (May 31, 2025)

## 🗂️ Repository Structure

```plaintext
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── src
│   ├── agent_execution
│   │   └── main.py   # Main execution script for the AI agent
│   ├── auth
│   │   └── authentication_setup.py  # Handles environment variable setup
│   ├── graph
│   │   ├── agent_graph.py  # Configures and builds an agent graph
│   │   └── main_agent_graph.png  # Flowchart depicting graph interactions
│   ├── prompts
│   │   └── prompt_template.py  # Defines system and human prompt templates
│   └── tools
│       └── tool_util.py  # Contains utility functions for tool integration
├── tests
│   └── unit_test.py   # Unit tests for validating tool functionality
```
