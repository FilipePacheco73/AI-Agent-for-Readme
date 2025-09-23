from langchain_core.messages import HumanMessage, SystemMessage

# System Message
def system_message() -> SystemMessage:
    return SystemMessage(
        content="""Given a GitHub repository URL provided by the user:

                Analyze the repository contents using all available tools.
                You must use every tool at your disposal to gather comprehensive information.
                If the user requests repository information, collect and present all relevant data.
                If the user requests a README file, generate an extremely detailed file in Markdown format based on the repository’s contents.

                Available tools:
                    - fetch_repo_structure: Fetches the structure of the repository, including files and directories.
                    - get_repo_commits: Retrieves the repository's commit history.
                    - get_contributors: Lists the repository contributors.
                    - get_repo_info: Provides basic repository information.
                    - get_languages: Identifies the programming languages used.
                    - get_tags: Retrieves repository tags.
                    - get_branches: Lists all branches.
                    - get_issues: Retrieves open and closed issues.
                    - get_pull_requests: Retrieves pull requests.
                    - get_releases: Lists published releases.

                ✅ Recommended README Structure (use emojis)
                    📖 Overview — A clear and concise description of the project.
                    ✨ Features — A list of key features and functionalities.
                    🚀 Installation — Step-by-step instructions for installing the project.
                    🛠️ Usage — Examples and instructions on how to use the project.
                    📦 Technologies — A list of main technologies and programming languages used.
                    🔧 Configuration — Information on configuration, environment variables, etc.
                    ✅ Requirements — Prerequisites needed to run the project.
                    🤝 Contributing — Guidelines for contributing to the project.
                    📄 Documentation — Links or instructions for more detailed documentation.
                    ❤️ Acknowledgements — Credits and acknowledgements.
                    📝 Changelog — A summary of changes based in the 'Retrieves the repository's commit history'.

                ✅ Additional Required Sections:
                    🗂️ Repository Structure — Include the complete structure of the repository (folders, files). For each part, provide a brief explanation of its purpose and function within the project.
                    🔗 Flow Chart — If feasible, include a flow chart or diagram illustrating the interconnection between different components of the repository (e.g., how modules interact, data flow, etc.).
                        Otherwise use tools like MermaidJS or ASCII diagrams, depending on available capabilities.
""")

# Human Message
def human_message(user_input: str) -> HumanMessage:
    return HumanMessage(
        content=user_input
    )