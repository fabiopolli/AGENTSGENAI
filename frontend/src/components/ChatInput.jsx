import React from 'react';
   export default function ChatInput({ onSend }) {
       const [input, setInput] = React.useState('');
       return (
          <div className="flex gap-2 mt-4">
               <input className="border rounded-lg p-2 w-full" value={input} onChange={(e) => setInput(e.target.value)} placeholder="Digite sua pergunta..."/>
               <button className="bg-blue-500 text-white p-2 rounded-lg" onClick={() => onSend(input)}>Enviar</button>
           </div>
       );
   }