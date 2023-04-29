import "@/styles/globals.css";
import type { AppProps } from "next/app";
import AppLayout from "@/layouts/AppLayout";
import Head from "next/head";

export default function App({ Component, pageProps }: AppProps) {
  return (
    <AppLayout>
      <Head>
        <title>Meyfu</title>
        <link rel="shortcut icon" href="logo.svg" type="image/x-icon" />
      </Head>
      <Component {...pageProps} />
    </AppLayout>
  )
}
