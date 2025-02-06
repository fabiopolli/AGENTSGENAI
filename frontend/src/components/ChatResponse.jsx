import React from "react";

export default function ChatResponse({ response }) {
  if (!response) return null;

  return (
    <div className="mt-4 p-4 bg-white shadow rounded w-full max-w-2xl border border-gray-300">
      <strong>Resposta:</strong>
      <p className="text-gray-700 mt-2">{response}</p>
    </div>
  );
}
