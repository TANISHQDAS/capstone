import { NextResponse } from 'next/server';

export const runtime = 'nodejs';

const MAX_VIDEO_BYTES = 20 * 1024 * 1024;

export async function POST(request: Request) {
  try {
    const formData = await request.formData();
    const file = formData.get('file');

    if (!(file instanceof File)) {
      return NextResponse.json({ message: 'Choose a PDF, transcript, or video file.' }, { status: 400 });
    }

    const buffer = Buffer.from(await file.arrayBuffer());
    const isPdf = file.type === 'application/pdf' || file.name.toLowerCase().endsWith('.pdf');
    const isVideo = file.type.startsWith('video/') || /\.(mp4|webm|mov|m4v)$/i.test(file.name);

    if (isVideo) {
      if (buffer.byteLength > MAX_VIDEO_BYTES) {
        return NextResponse.json({ message: 'Video uploads must be 20 MB or smaller.' }, { status: 413 });
      }

      const apiKey = process.env.GEMINI_API_KEY;
      if (!apiKey) {
        return NextResponse.json({ message: 'Video transcription is not configured. Add GEMINI_API_KEY to the server environment.' }, { status: 503 });
      }

      const response = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            contents: [{
              parts: [
                { text: 'Transcribe the spoken meeting in this video. Return only the transcript with speaker names when identifiable. Do not summarize.' },
                { inlineData: { mimeType: file.type || 'video/mp4', data: buffer.toString('base64') } }
              ]
            }]
          })
        }
      );
      const data = await response.json();
      if (!response.ok) {
        return NextResponse.json({ message: data.error?.message || 'Video transcription failed.' }, { status: 502 });
      }

      const transcript = data.candidates?.[0]?.content?.parts?.[0]?.text?.trim();
      if (!transcript) {
        return NextResponse.json({ message: 'No speech was detected in this video.' }, { status: 422 });
      }
      return NextResponse.json({ text: transcript, fileName: file.name });
    }

    let text = buffer.toString('utf-8');
    if (isPdf) {
      const pdfParse = (await import('pdf-parse/lib/pdf-parse')).default;
      text = (await pdfParse(buffer)).text;
    }
    const cleanedText = text.replace(/\s+/g, ' ').trim();

    if (!cleanedText) {
      return NextResponse.json({ message: 'No readable text was found in this file.' }, { status: 422 });
    }

    return NextResponse.json({ text: cleanedText, fileName: file.name });
  } catch (error) {
    console.error('Transcript extraction failed:', error);
    return NextResponse.json({ message: 'Could not read this file.' }, { status: 400 });
  }
}
