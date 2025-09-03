# Gentmini

A minimal AI Agent using Gemini. Built from scratch in Python for learning purposes.

## Learning Goals

The learning goals of this project are:

1. Introduce us to multidirectory Python projects
2. Understand how the AI tools that we'll almost certainly use on the job actually work under the hood
3. Practice our Python and functional programming skills

The goal is not to build an LLM from scratch, but to instead use a pre-trained LLM to build an agent from scratch.

## How It Works

The agent uses Gemini API to process user input and generate responses. It will only work on a specified working directory defined in `config.py` (a simple calculator app in this case). The agent can call a set of predefined functions, which are defined in the `functions` directory. For this project, the agent can get files info, read a file, write to a file, and run Python code.

## Project Structure

The project is structured as follows:

```md
gentmini/
├── calculator/                 # A simple calculator app. Used for agent's working directory
├── functions/                  # Functions that the agent can call
│   ├── function_schema.py      # Function schemas for declaration
│   ├── get_file_content.py     
│   ├── get_files_info.py
│   ├── run_python.py
│   └── write_file.py         
├── call.py                     # Function that agent uses to call functions
├── config.py                   # Configuration file for the project
├── main.py                     # Main entry point for the agent
├── pyproject.toml              # Project metadata and dependencies
├── tests.py                    # Tests for the project
├── .gitignore                  # Files to ignore in git
└── README.md                   # This file
```

## Prerequisites

<details>
  <summary> Install <code><a href="https://docs.astral.sh/uv/">uv</a></code> package manager</summary>

### Install with curl

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Install with wget

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

### Install on Windows (PowerShell)

Use `irm` to download the script and execute it with `iex`:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

</details>

## Setup and Run

1. Clone the repository:

   ```bash
   git clone https://github.com/babanini95/gentmini.git
   ```

2. Navigate to the project directory:

   ```bash
   cd gentmini
   ```

3. Configure your environment variables. Create a `.env` file in the root directory and add your Gemini API key:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

4. Install the required dependencies:

   ```bash
   uv sync
   ```

5. Run the agent:

   ```bash
   uv run main.py "Your task here"
   ```
