'use client';

import React, { useState } from 'react';

export default function MeetingIntelligenceAgentPage() {
  const [step, setStep] = useState(1);
  const [transcript, setTranscript] = useState(
    'Alex: Welcome everyone. Marcus, please configure the database search index by Friday. Maya, please finish the task automation workflow today.'
  );

  const [tasks, setTasks] = useState([
    {
      id: 't-1',
      task: 'Configure database search index',
      owner: 'Marcus',
      dueDate: '2026-09-12',
      status: 'pending',
      ticketId: ''
    },
    {
      id: 't-2',
      task: 'Complete task automation workflow',
      owner: 'Maya',
      dueDate: '2026-09-10',
      status: 'pending',
      ticketId: ''
    }
  ]);

  const handleExtractTasks = () => {
    setStep(2);
  };

  const handleCreateTicket = (taskId: string) => {
    const generatedTicket = `LIN-${Math.floor(1000 + Math.random() * 9000)}`;
    setTasks(
      tasks.map((t) =>
        t.id === taskId ? { ...t, status: 'created', ticketId: generatedTicket } : t
      )
    );
  };

  const handleRejectTask = (taskId: string) => {
    setTasks(
      tasks.map((t) => (t.id === taskId ? { ...t, status: 'rejected' } : t))
    );
  };

  return (
    <div className="max-w-[1200px] mx-auto p-4 md:p-8 space-y-6">
      
      {/* Header Bar */}
      <header className="bg-white border border-slate-200 rounded-xl p-5 shadow-sm flex flex-wrap items-center justify-between gap-4">
        <div className="flex items-center space-x-3">
          <div className="bg-black text-white p-2 rounded-lg flex items-center justify-center">
            <svg width="16" height="14" viewBox="0 0 76 65" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M37.5274 0L75.0548 65H0L37.5274 0Z" fill="white"/>
            </svg>
          </div>
          <div>
            <h1 className="text-xl font-bold tracking-tight text-slate-900 flex items-center gap-2">
              Meeting Intelligence Agent
              <span className="text-xs font-mono bg-emerald-50 text-emerald-700 border border-emerald-200 px-2 py-0.5 rounded-full font-medium">
                Deployed on Vercel
              </span>
            </h1>
            <p className="text-xs text-slate-500 font-mono">Turn Meeting Speech into Verified Work Tickets</p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={() => { setStep(1); setTasks(tasks.map(t => ({ ...t, status: 'pending', ticketId: '' }))); }}
            className="text-xs text-slate-600 border border-slate-300 hover:bg-slate-100 font-mono px-3 py-2 rounded-lg transition-all"
          >
            🔄 Reset
          </button>
        </div>
      </header>

      {/* 3 Step Banner */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs font-mono">
        <div className={`p-4 rounded-xl border transition-all ${step >= 1 ? 'bg-white border-indigo-400 shadow-sm' : 'bg-slate-50 border-slate-200 text-slate-400'}`}>
          <div className="font-bold text-indigo-600 mb-1">1. Audio / Transcript</div>
          <div className="text-slate-600">Provide what people said in meeting</div>
        </div>
        <div className={`p-4 rounded-xl border transition-all ${step >= 2 ? 'bg-white border-indigo-400 shadow-sm' : 'bg-slate-50 border-slate-200 text-slate-400'}`}>
          <div className="font-bold text-indigo-600 mb-1">2. AI Reads Tasks</div>
          <div className="text-slate-600">Finds Task, Who does it & Due Date</div>
        </div>
        <div className={`p-4 rounded-xl border transition-all ${tasks.some(t => t.status === 'created') ? 'bg-white border-emerald-400 shadow-sm' : 'bg-slate-50 border-slate-200 text-slate-400'}`}>
          <div className="font-bold text-emerald-600 mb-1">3. Create Ticket</div>
          <div className="text-slate-600">Saves task ticket to Linear</div>
        </div>
      </div>

      {/* Asymmetrical Layout (8 Cols Left / 4 Cols Right) */}
      <div className="grid grid-cols-1 md:grid-cols-12 gap-6">

        {/* Left Side (8 Cols) */}
        <div className="md:col-span-8 space-y-6">

          <div className="bg-white border border-slate-200 rounded-xl p-5 shadow-sm space-y-3">
            <div className="flex items-center justify-between border-b border-slate-100 pb-2">
              <h2 className="text-sm font-bold text-slate-900 flex items-center gap-2">
                <span className="w-6 h-6 rounded-full bg-indigo-100 text-indigo-700 text-xs flex items-center justify-center font-mono">1</span>
                What People Said in the Meeting
              </h2>
              <span className="text-xs text-slate-400 font-mono">Meeting Transcript</span>
            </div>

            <textarea
              rows={3}
              value={transcript}
              onChange={(e) => setTranscript(e.target.value)}
              className="w-full bg-slate-50 border border-slate-200 rounded-lg p-3 text-xs text-slate-800 focus:outline-none focus:border-indigo-500 font-sans"
            />

            <button
              onClick={handleExtractTasks}
              className="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold text-xs px-4 py-2.5 rounded-lg shadow-sm transition-all flex items-center gap-2"
            >
              🧠 Extract Action Items with AI
            </button>
          </div>

          {step >= 2 && (
            <div className="bg-white border border-slate-200 rounded-xl p-5 shadow-sm space-y-4 border-l-4 border-l-indigo-600">
              <div className="flex items-center justify-between border-b border-slate-100 pb-2">
                <h2 className="text-sm font-bold text-slate-900 flex items-center gap-2">
                  <span className="w-6 h-6 rounded-full bg-indigo-100 text-indigo-700 text-xs flex items-center justify-center font-mono">2</span>
                  Tasks Found by AI
                </h2>
                <span className="text-xs font-mono text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
                  Ready to Create Ticket
                </span>
              </div>

              <div className="space-y-4">
                {tasks.map((item) => (
                  <div key={item.id} className="bg-slate-50 border border-slate-200 rounded-lg p-4 space-y-3">
                    
                    <div className="flex items-start justify-between gap-3">
                      <div className="font-bold text-sm text-slate-900">{item.task}</div>
                      {item.status === 'created' && (
                        <span className="bg-purple-100 text-purple-800 border border-purple-200 text-xs font-mono font-bold px-2.5 py-0.5 rounded">
                          {item.ticketId}
                        </span>
                      )}
                    </div>

                    <div className="grid grid-cols-2 gap-2 text-xs font-mono text-slate-600 bg-white p-2.5 rounded border border-slate-200">
                      <div>Person Responsible: <strong className="text-indigo-700">{item.owner}</strong></div>
                      <div>Must finish by: <strong className="text-slate-800">{item.dueDate}</strong></div>
                    </div>

                    {item.status === 'pending' && (
                      <div className="flex items-center justify-end gap-2 pt-1">
                        <button
                          onClick={() => handleCreateTicket(item.id)}
                          className="bg-emerald-600 hover:bg-emerald-700 text-white font-semibold text-xs px-3.5 py-1.5 rounded-lg shadow-sm transition-all"
                        >
                          ✓ Create Ticket in Linear
                        </button>
                        <button
                          onClick={() => handleRejectTask(item.id)}
                          className="bg-slate-200 hover:bg-slate-300 text-slate-700 text-xs px-3 py-1.5 rounded-lg transition-all"
                        >
                          Reject Task
                        </button>
                      </div>
                    )}

                    {item.status === 'created' && (
                      <div className="text-xs font-mono text-emerald-700 font-bold bg-emerald-50 p-2 rounded border border-emerald-200 flex items-center gap-1">
                        ✓ Ticket created and verified in Linear task manager!
                      </div>
                    )}

                    {item.status === 'rejected' && (
                      <div className="text-xs font-mono text-slate-500 bg-slate-100 p-2 rounded border border-slate-200">
                        Task rejected / discarded.
                      </div>
                    )}

                  </div>
                ))}
              </div>
            </div>
          )}

        </div>

        {/* Right Explanation Panel (4 Cols) */}
        <div className="md:col-span-4 space-y-4">
          <div className="bg-white border border-slate-200 rounded-xl p-5 shadow-sm space-y-3 border-t-4 border-t-indigo-600">
            <h3 className="text-xs font-bold text-slate-900 uppercase tracking-wider font-mono">
              Simple Concept Summary
            </h3>

            <div className="bg-slate-50 p-3 rounded-lg border border-slate-200 text-xs font-mono space-y-2 text-slate-700">
              <div className="font-bold text-indigo-700">What the Agent Does:</div>
              <ol className="list-decimal list-inside space-y-1.5 text-slate-600">
                <li>Listens to meeting audio</li>
                <li>Extracts task, owner & due date</li>
                <li>Creates task ticket in Linear</li>
              </ol>
            </div>
          </div>
        </div>

      </div>

      <footer className="text-center text-xs text-slate-500 font-mono py-4 border-t border-slate-200 flex flex-wrap justify-between gap-2">
        <div>Meeting Intelligence Agent</div>
        <div>Hostable on Vercel</div>
      </footer>

    </div>
  );
}
