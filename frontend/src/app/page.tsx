export default function Home(): React.JSX.Element {
  return (
    <main className="mx-auto flex min-h-screen w-full max-w-5xl flex-col justify-center gap-6 px-8 py-16">
      <p className="text-sm uppercase tracking-[0.2em] text-zinc-500">LEVIT v2</p>
      <h1 className="text-4xl font-semibold text-zinc-100 md:text-5xl">Phase 1 Infrastructure Ready</h1>
      <p className="max-w-3xl text-lg text-zinc-400">
        Frontend and backend packages are initialized independently with a deep-dark UI baseline
        (#0A0A0A), typed backend settings, and LangGraph-ready orchestration scaffolding.
      </p>
    </main>
  );
}
