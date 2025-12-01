#!/usr/bin/env python3
"""
Test script to verify Anthropic API key works
"""

import os
import sys
from anthropic import Anthropic


def test_api_key(api_key):
    """Test if the API key works by making a simple API call."""
    try:
        client = Anthropic(api_key=api_key)

        # Make a simple test request
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=100,
            messages=[
                {
                    "role": "user",
                    "content": "Say 'API key is valid!' if you can read this."
                }
            ]
        )

        print("✅ API Key Test Successful!")
        print(f"Response: {message.content[0].text}")
        return True

    except Exception as e:
        print(f"❌ API Key Test Failed!")
        print(f"Error: {str(e)}")
        return False


if __name__ == "__main__":
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    success = test_api_key(api_key)
    sys.exit(0 if success else 1)
