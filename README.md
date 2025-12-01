# The Real Onezz

A powerful Strands Agent implementation for real-world AI tasks.

## Overview

This project implements a Strands agent that demonstrates how to create, configure, and deploy intelligent agents using the Strands SDK.

## Setup

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/the-reall-onezz.git
cd "the reall onezz"
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the agent in interactive mode:
```bash
python agent.py
```

## Configuration

### Model Provider

The agent can use different model providers:

- **Ollama** (Local): Default configuration uses Ollama with Llama2
- **AWS Bedrock**: Configure with `model_provider="bedrock"`

### Environment Variables

Create a `.env` file to configure:
```
STRANDS_MODEL_PROVIDER=ollama
STRANDS_MODEL_ID=llama2
```

## Project Structure

```
the reall onezz/
├── agent.py              # Main agent implementation
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── .gitignore          # Git ignore rules
└── .env.example        # Environment variables template
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License

## Author

Frank Simpson
