import './globals.css';

export const metadata = {
  title: 'Conversational Shopping Concierge',
  description: 'Multi-agent shopping assistant',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
