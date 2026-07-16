
# Ai-Agent-v2

An AI agent application built with Python and Flask, powered by the Groq API (Llama 3.3 70B). The agent supports tool-calling capabilities and is deployed on Vercel.

**Live demo:** https://ai-agent-v2-tau.vercel.app/

## Overview

Ai-Agent-v2 is a conversational AI agent that processes natural language input, determines when external tools are required, executes those tools, and returns a synthesized response. The project is structured for easy extension, allowing new tools to be registered without modifying the core agent logic.

## Features

- Natural language chat interface
- LLM-powered responses using the Groq API (Llama 3.3 70B Versatile)
- Tool-calling architecture for extending agent capabilities
- Modular codebase separating configuration, LLM logic, tools, and application routes
- Deployed and accessible via Vercel

## Tech Stack

- **Backend:** Python, Flask
- **LLM Provider:** Groq (OpenAI-compatible API)
- **Model:** llama-3.3-70b-versatile
- **Deployment:** Vercel
- **Environment Management:** python-dotenv

## Project Structure

```
Ai-AGENT-II/
├── api/                # API entry points
├── data/                # Application data
├── static/              # Static assets
├── tools/                # Tool implementations (e.g. weather)
│   └── registry.py       # Tool registration and execution
├── venv/                 # Virtual environment (not tracked)
├── agent.py              # Core agent logic
├── app.py                # Flask application entry point
├── config.py              # Configuration and environment variable loading
├── llm.py                 # LLM client and chat completion logic
├── memory.py               # Conversation memory handling
├── parser.py               # Input/output parsing utilities
├── prompts.py               # System and tool prompts
├── requirements.txt          # Python dependencies
├── vercel.json                # Vercel deployment configuration
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.11 or higher
- A Groq API key (obtainable from console.groq.com)

### Installation

1. Clone the repository

```bash
git clone https://github.com/nikhil965/Ai-Agent-v2.git
cd Ai-Agent-v2
```

2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure environment variables

Create a `.env` file in the project root with the following content:

```
GROQ_API_KEY=your_groq_api_key_here
```

### Running Locally

```bash
python app.py
```

The application will start a local Flask server. Open the displayed local URL in a browser to interact with the agent.

## Configuration

Configuration values are defined in `config.py` and loaded from environment variables:

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | API key used to authenticate with the Groq API |
| `BASE_URL` | Base URL for the Groq OpenAI-compatible endpoint |
| `MODEL_NAME` | Model identifier used for chat completions |

## Deployment

This project is configured for deployment on Vercel using `vercel.json`. To deploy your own instance:

1. Fork or clone this repository
2. Import the project into Vercel
3. Add `GROQ_API_KEY` as an environment variable in the Vercel project settings
4. Deploy

## Adding New Tools

Tools are defined in the `tools/` directory and registered in `tools/registry.py`. To add a new tool:

1. Create a new file in `tools/` implementing an `execute` function
2. Import and register the tool in `registry.py`
3. Update `prompts.py` if the agent needs to be made aware of the new tool's purpose

## License

This project does not currently specify a license. Add a `LICENSE` file if you intend to make usage terms explicit.

## Contributing

Contributions are welcome. Please open an issue to discuss proposed changes before submitting a pull request.
