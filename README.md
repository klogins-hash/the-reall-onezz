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

This agent uses **Anthropic Claude Haiku 4.5** (claude-haiku-4-5-20251001) as the default model provider - the latest available Claude Haiku model.

### Environment Variables

Before running the agent, set your Anthropic API key:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

Or create a `.env` file:
```
ANTHROPIC_API_KEY=your-api-key-here
```

You can obtain an API key from [Anthropic Console](https://console.anthropic.com)

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
