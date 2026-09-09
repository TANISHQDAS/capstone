import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Meeting Intelligence Agent Dashboard',
  description: 'Closed-loop task extraction, Slack approval, and ticket verification dashboard',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-[#0f1b2a] text-[#f2f3f3] antialiased min-h-screen">
        {children}
      </body>
    </html>
  );
}
