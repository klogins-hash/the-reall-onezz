#!/usr/bin/env python3
"""
The Real Onezz - A Strands Agent Implementation
Uses Anthropic Claude Haiku 4.5 as the model provider
"""

import os
from strands_agents import Agent


def create_agent():
    """Create and configure a Strands agent with Anthropic Claude Haiku."""

    # Ensure API key is set
    if not os.getenv("ANTHROPIC_API_KEY"):
        raise ValueError(
            "ANTHROPIC_API_KEY environment variable is not set. "
            "Please set it before running the agent."
        )

    # Create the agent with Anthropic Claude Haiku configuration
    agent = Agent(
        name="The Real Onezz",
        description="A powerful Strands agent powered by Claude Haiku 4.5",
        model_provider="anthropic",
        model_config={"model_id": "claude-3-5-haiku-20241022"}
    )

    return agent


def main():
    """Main entry point for the agent."""
    agent = create_agent()

    # Start interactive mode
    print("Welcome to The Real Onezz - Your Strands Agent!")
    print("Type 'exit' to quit, or ask your question...\n")

    while True:
        try:
            user_input = input("> ").strip()

            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            if not user_input:
                continue

            # Process the query through the agent
            response = agent.query(user_input)
            print(f"\nAgent: {response}\n")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
