import React, { useState } from 'react';
import ChatInput from '../components/ChatInput';

export default function Home() {
    const [response, setResponse] = useState('');
    const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

    console.log("API URL:", API_URL);

    const handleSend = async (input) => {
        console.log("Enviando pergunta:", input);
        try {
            const res = await fetch(`${API_URL}/chat`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question: input })
            });

            if (!res.ok) {
                throw new Error(`Erro ao conectar com a API: ${res.status}`);
            }

            const data = await res.json();
            console.log("Dados recebidos:", data);

            if (data && typeof data.response === "object" && "response" in data.response) {
                setResponse(data.response.response);
            } else {
                setResponse("Erro ao processar a resposta.");
            }

        } catch (error) {
            console.error("Erro na requisição:", error);
            setResponse("Erro ao conectar com o servidor. Verifique a conexão.");
        }
    };

    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50 p-4">
            {/* ✅ Logo na parte superior */}
            <img src="/logo.png" alt="Logo" className="w-40 mb-4" />

            <h1 className="text-2xl font-bold mb-4">Chat com Assistente</h1>
            <ChatInput onSend={handleSend} />

            {response && (
                <div className="mt-4 p-4 bg-white shadow rounded w-full max-w-2xl border border-gray-300">
                    <strong>Resposta:</strong>
                    <p className="text-gray-700 mt-2">{response}</p>
                </div>
            )}
        </div>
    );
}
