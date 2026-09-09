import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Meeting Intelligence Agent',
  description: 'Turn Meeting Audio & Speech into Verified Work Tickets',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-slate-50 text-slate-900 antialiased min-h-screen">
        {children}
      </body>
    </html>
  );
}
