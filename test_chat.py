#!/usr/bin/env python3
"""
Test chat script to interact with Pepper Potts agent
Demonstrates the personality and capabilities of The Real Onezz
"""

import os
import sys
from anthropic import Anthropic

# Pepper Potts system prompt
PEPPER_PROMPT = """You are Pepper Potts, CEO and voice of reason. You're intelligent, organized, and pragmatic -
someone who gets things done with precision and grace under pressure. You have a sharp wit and aren't afraid to
call out bad ideas, but you do so with charm and professionalism. You're resourceful, analytical, and always thinking
three steps ahead. When helping users, you're direct but diplomatic, offering practical solutions while maintaining
sophistication. You bring order to chaos and wisdom to difficult decisions. Think of yourself as the capable leader
who makes everything work, with a dash of sass when appropriate."""


def test_pepper_chat():
    """Test chat with Pepper Potts personality."""
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        print("Please set it before running this test:")
        print('  export ANTHROPIC_API_KEY="your-api-key-here"')
        sys.exit(1)

    client = Anthropic(api_key=api_key)

    print("=" * 60)
    print("🎯 Testing Pepper Potts Agent - The Real Onezz")
    print("=" * 60)
    print("\n✨ Pepper is online and ready to help!\n")

    # Test queries to showcase personality
    test_queries = [
        "Hi Pepper, what's your approach to solving complex problems?",
        "I have a bad idea - should I share it anyway?",
        "How do you stay organized when everything is chaotic?",
        "What's your take on work-life balance?"
    ]

    for i, query in enumerate(test_queries, 1):
        print(f"\n{'─' * 60}")
        print(f"📝 Question {i}: {query}")
        print("─" * 60)

        try:
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=300,
                system=PEPPER_PROMPT,
                messages=[
                    {"role": "user", "content": query}
                ]
            )

            answer = response.content[0].text
            print(f"\n💬 Pepper: {answer}\n")

        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")
            return False

    print("\n" + "=" * 60)
    print("✅ Test Complete! Pepper Potts is working perfectly!")
    print("=" * 60)
    return True


if __name__ == "__main__":
    success = test_pepper_chat()
    sys.exit(0 if success else 1)
