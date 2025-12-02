# The Real Onezz - Web Chat Interface

A modern web chat interface for Pepper Potts AI agent, built with Next.js and shadcn/ui.

## Features

- 🎨 Beautiful dark-themed chat interface
- ⚡ Real-time messaging with Pepper Potts
- 🔐 Secure API integration with Anthropic Claude
- 📱 Responsive design
- ⌨️ Real-time typing with message history
- 🎯 Pepper's pragmatic personality in every response

## Tech Stack

- **Frontend:** Next.js 14, React 18, TypeScript
- **Styling:** Tailwind CSS
- **UI Components:** shadcn/ui patterns
- **AI:** Anthropic Claude Haiku 4.5
- **Deployment:** Ready for Vercel, Docker, or standard Node servers

## Quick Start

### Prerequisites

- Node.js 18+ or 20+
- npm, yarn, or pnpm
- Anthropic API key

### Installation

1. Navigate to the web directory:
```bash
cd web
```

2. Install dependencies:
```bash
npm install
# or
yarn install
# or
pnpm install
```

3. Set up environment variables:
```bash
cp .env.example .env.local
```

4. Add your Anthropic API key to `.env.local`:
```
ANTHROPIC_API_KEY=your_api_key_here
```

### Development

Run the development server:
```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) to chat with Pepper!

### Production Build

```bash
npm run build
npm start
```

## API Routes

### POST `/api/chat`

Send a message to Pepper Potts.

**Request:**
```json
{
  "message": "Your question here",
  "history": [
    {
      "id": "1",
      "role": "user",
      "content": "Previous user message",
      "timestamp": "2025-12-01T..."
    },
    {
      "id": "2",
      "role": "assistant",
      "content": "Previous assistant response",
      "timestamp": "2025-12-01T..."
    }
  ]
}
```

**Response:**
```json
{
  "message": "Pepper's response"
}
```

## Deployment

### Deploy to Vercel

1. Push to GitHub
2. Connect your repository to Vercel
3. Set `ANTHROPIC_API_KEY` environment variable in Vercel dashboard
4. Deploy!

### Deploy with Docker

```bash
docker build -t pepper-potts-web .
docker run -e ANTHROPIC_API_KEY=your_key -p 3000:3000 pepper-potts-web
```

### Self-hosted

1. Build the app: `npm run build`
2. Copy the `.next` directory and necessary files to your server
3. Install production dependencies: `npm ci --omit=dev`
4. Set environment variables
5. Start with: `npm start`

## Project Structure

```
web/
├── app/
│   ├── api/
│   │   └── chat/
│   │       └── route.ts          # Chat API endpoint
│   ├── globals.css               # Global styles
│   ├── layout.tsx                # Root layout
│   └── page.tsx                  # Main chat interface
├── package.json
├── tailwind.config.js
├── next.config.js
├── .env.example
└── README.md
```

## Customization

### Change the Model

Edit `/app/api/chat/route.ts` and change:
```typescript
model: 'claude-haiku-4-5-20251001',
```

### Adjust Pepper's Personality

Edit the `PEPPER_PROMPT` variable in `/app/api/chat/route.ts` to customize Pepper's personality.

### Styling

Colors and theme are defined in `tailwind.config.js` and `app/globals.css`. Modify as needed.

## Environment Variables

Required:
- `ANTHROPIC_API_KEY` - Your Anthropic API key

Optional:
- `NODE_ENV` - Set to `production` for production builds

## Troubleshooting

**API Key not working:**
- Ensure `ANTHROPIC_API_KEY` is set in `.env.local`
- Check that the key is valid in Anthropic console
- Restart the development server after changing env vars

**Chat not responding:**
- Check browser console for errors
- Verify network tab shows requests to `/api/chat`
- Check server logs for error messages

**Styling issues:**
- Clear `.next` cache: `rm -rf .next`
- Rebuild: `npm run build`

## License

MIT

## Support

For issues or questions, check the main repository or create an issue on GitHub.
