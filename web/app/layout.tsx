import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Pepper Potts - The Real Onezz',
  description: 'Chat with Pepper Potts - pragmatic AI decision maker',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="bg-slate-950 text-white">{children}</body>
    </html>
  )
}
