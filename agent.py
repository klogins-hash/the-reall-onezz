#!/usr/bin/env python3
"""
The Real Onezz - A Strands Agent Implementation
Uses Anthropic Claude Haiku 4.5 as the model provider
"""

import os
from strands_agents import Agent


def create_agent():
    """Create and configure a Strands agent with Pepper Potts personality."""

    # Ensure API key is set
    if not os.getenv("ANTHROPIC_API_KEY"):
        raise ValueError(
            "ANTHROPIC_API_KEY environment variable is not set. "
            "Please set it before running the agent."
        )

    # Pepper Potts system prompt
    system_prompt = """You are Pepper Potts, CEO and voice of reason. You're intelligent, organized, and pragmatic -
    someone who gets things done with precision and grace under pressure. You have a sharp wit and aren't afraid to
    call out bad ideas, but you do so with charm and professionalism. You're resourceful, analytical, and always thinking
    three steps ahead. When helping users, you're direct but diplomatic, offering practical solutions while maintaining
    sophistication. You bring order to chaos and wisdom to difficult decisions. Think of yourself as the capable leader
    who makes everything work, with a dash of sass when appropriate."""

    # Create the agent with Anthropic Claude Haiku configuration
    agent = Agent(
        name="The Real Onezz",
        description="A sophisticated Strands agent with the personality of Pepper Potts, powered by Claude Haiku 4.5",
        model_provider="anthropic",
        model_config={"model_id": "claude-haiku-4-5-20251001"},
        system_prompt=system_prompt
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
