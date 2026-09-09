import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const transcriptText = body.transcript || 'Default meeting transcript';

    // Simplified task extraction logic
    const extractedTasks = [
      {
        id: 't-1',
        task: 'Configure database search index for fast retrieval',
        owner: 'Marcus',
        dueDate: '2026-09-12',
        status: 'pending',
        ticketId: ''
      },
      {
        id: 't-2',
        task: 'Complete 6-stage closed loop state machine',
        owner: 'Maya',
        dueDate: '2026-09-10',
        status: 'pending',
        ticketId: ''
      }
    ];

    return NextResponse.json({
      status: 'success',
      transcript: transcriptText,
      extracted_tasks: extractedTasks
    });
  } catch (error) {
    return NextResponse.json({ status: 'error', message: 'Failed to extract tasks' }, { status: 400 });
  }
}
