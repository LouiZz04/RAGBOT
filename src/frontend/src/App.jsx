import { useMemo, useState } from "react";
import ReactMarkdown from "react-markdown";
import "./App.css";

const MAX_PDF_MB = 25;
const MAX_PDF_BYTES = MAX_PDF_MB * 1024 * 1024;

export default function App() {
  const [pdfFile, setPdfFile] = useState(null);
  const [status, setStatus] = useState("idle"); // idle | selected | processing | ready
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const canSend = useMemo(
    () => !!pdfFile && status !== "processing",
    [pdfFile, status]
  );
  const canAsk = status === "ready";

  function handlePickFile(e) {
    const file = e.target.files?.[0] ?? null;
    if (!file) return;

    if (file.type !== "application/pdf") {
      alert("Please select a PDF file.");
      e.target.value = "";
      return;
    }

    if (file.size > MAX_PDF_BYTES) {
      alert(`PDF is too large. Max allowed: ${MAX_PDF_MB} MB.`);
      e.target.value = "";
      return;
    }

    setPdfFile(file);
    setStatus("selected");
    setQuestion("");
    setAnswer("");
  }

  function handleRemoveFile() {
    setPdfFile(null);
    setStatus("idle");
    setQuestion("");
    setAnswer("");
  }

  async function handleSend() {
    if (!pdfFile) return;

    setStatus("processing");
    setAnswer("");

    const formData = new FormData();
    formData.append("files", pdfFile);

    try {
      const res = await fetch("http://localhost:8000/upload", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) throw new Error("Upload failed");

      const data = await res.json();
      console.log("Indexed:", data);
      setStatus("ready");
    } catch (err) {
      console.error(err);
      setStatus("selected"); // Go back to selected on error
      alert("Error uploading file.");
    }
  }

  async function handleAsk() {
    if (!canAsk || question.trim().length === 0) return;
    setAnswer("Thinking...");

    try {
      // Note: Backend expects query param `question`
      const res = await fetch(`http://localhost:8000/ask?question=${encodeURIComponent(question)}`, {
        method: "POST"
      });

      if (!res.ok) throw new Error("Ask failed");

      const data = await res.json();
      setAnswer(data.answer);
    } catch (err) {
      console.error(err);
      setAnswer("Error getting answer.");
    }
  }

  return (
    <div className="page">
      <header className="header">
        <div className="brandDot" />
        <div>
          <h1 className="title">PDF RAG</h1>
          <p className="subtitle">Upload • Process • Ask</p>
        </div>
      </header>

      <main className="layout">
        {/* Upload */}
        <section className="card">
          <div className="cardTop">
            <h2 className="cardTitle">Upload PDF</h2>
            <span className={`pill pill-${status}`}>
              {status === "idle" && "Idle"}
              {status === "selected" && "Ready to send"}
              {status === "processing" && "Processing"}
              {status === "ready" && "Ready"}
            </span>
          </div>

          <div className={`dropArea ${status === "processing" ? "disabled" : ""}`}>
            <label className="fileLabel">
              <input
                type="file"
                accept="application/pdf"
                onChange={handlePickFile}
                disabled={status === "processing"}
              />
              <span className="fileLabelText">Choose PDF</span>
            </label>

            {pdfFile ? (
              <div className="fileInfo">
                <div className="fileText">
                  <div className="fileName">{pdfFile.name}</div>
                  <div className="fileMeta">
                    {(pdfFile.size / 1024 / 1024).toFixed(2)} MB
                  </div>
                </div>

                <button
                  className="btnGhost"
                  onClick={handleRemoveFile}
                  disabled={status === "processing"}
                >
                  Remove
                </button>
              </div>
            ) : (
              <p className="hint">
                Select a PDF (max {MAX_PDF_MB} MB) to enable Send.
              </p>
            )}
          </div>

          <div className="actions">
            <button className="btnPrimary" onClick={handleSend} disabled={!canSend}>
              {status === "processing" ? "Processing…" : "Send"}
            </button>

            <div className="statusText">
              {status === "idle" && "Select a PDF."}
              {status === "selected" && "Click Send to process."}
              {status === "processing" && "Please wait…"}
              {status === "ready" && "Ready."}
            </div>
          </div>
        </section>

        {/* Question */}
        <section className="card">
          <div className="cardTop">
            <h2 className="cardTitle">Question</h2>
          </div>

          <textarea
            className="textarea textareaTop"
            placeholder={canAsk ? "Type your question…" : "Waiting for processing…"}
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            disabled={!canAsk}
          />

          <div className="actions">
            <button
              className="btnPrimary"
              onClick={handleAsk}
              disabled={!canAsk || question.trim().length === 0}
            >
              Ask
            </button>
          </div>
        </section>
      </main>

      {/* Response */}
      <section className="card responseCard">
        <div className="cardTop">
          <h2 className="cardTitle">Response</h2>
        </div>

        <div className="responseBox">
          {status !== "ready" && <div className="responseMuted">No response yet.</div>}
          {status === "ready" && !answer && (
            <div className="responseMuted">Ask a question to see the response.</div>
          )}
          {!!answer && (
            <div className="responseText">
              <ReactMarkdown>{answer}</ReactMarkdown>
            </div>
          )}
        </div>
      </section>
    </div>
  );
}
