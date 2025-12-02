import { NextRequest, NextResponse } from 'next/server'

const PEPPER_PROMPT = `You are Pepper Potts, CEO and voice of reason. You're intelligent, organized, and pragmatic -
someone who gets things done with precision and grace under pressure. You have a sharp wit and aren't afraid to
call out bad ideas, but you do so with charm and professionalism. You're resourceful, analytical, and always thinking
three steps ahead. When helping users, you're direct but diplomatic, offering practical solutions while maintaining
sophistication. You bring order to chaos and wisdom to difficult decisions. Think of yourself as the capable leader
who makes everything work, with a dash of sass when appropriate.`

export async function POST(request: NextRequest) {
  try {
    const { message, history } = await request.json()

    if (!message) {
      return NextResponse.json(
        { error: 'Message is required' },
        { status: 400 }
      )
    }

    const apiKey = process.env.ANTHROPIC_API_KEY
    if (!apiKey) {
      return NextResponse.json(
        { error: 'API key not configured' },
        { status: 500 }
      )
    }

    // Format conversation history for Anthropic API
    const messages = history.map((msg: any) => ({
      role: msg.role === 'user' ? 'user' : 'assistant',
      content: msg.content,
    }))

    // Add the new user message
    messages.push({
      role: 'user',
      content: message,
    })

    // Call Anthropic API
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': apiKey,
        'anthropic-version': '2023-06-01',
      },
      body: JSON.stringify({
        model: 'claude-haiku-4-5-20251001',
        max_tokens: 1024,
        system: PEPPER_PROMPT,
        messages: messages,
      }),
    })

    if (!response.ok) {
      const error = await response.json()
      console.error('Anthropic API error:', error)
      return NextResponse.json(
        { error: 'Failed to get response from AI' },
        { status: response.status }
      )
    }

    const data = await response.json()
    const assistantMessage =
      data.content[0].type === 'text' ? data.content[0].text : ''

    return NextResponse.json({
      message: assistantMessage,
    })
  } catch (error) {
    console.error('Chat API error:', error)
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    )
  }
}
