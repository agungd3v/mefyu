import React from "react";
import { Inter } from "next/font/google";
import Navbar from "@/components/Navbar";

const f = Inter({ subsets: ['latin'] });

interface IProps {
  children: React.ReactNode;
}

export default function AppLayout({children}: IProps) {
  return (
    <div className={f.className}>
      <Navbar />
      <div>
        {children}
      </div>
    </div>
  )
}