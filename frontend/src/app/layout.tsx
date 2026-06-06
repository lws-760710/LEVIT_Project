import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "LEVIT v2 Console",
  description: "Deep-dark orchestration console baseline for LEVIT v2",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="h-full antialiased">
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}
