/**
 * AnswerBox Component
 *
 * Allows the candidate to answer
 * interview questions.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

import { useEffect, useState } from "react";
import useInterview from "../hooks/useInterview";

function AnswerBox({ questionId }) {
    const { answers, saveAnswer } = useInterview();

    const [answer, setAnswer] = useState("");

    useEffect(() => {
        setAnswer(answers[questionId] || "");
    }, [questionId, answers]);

    const handleChange = (e) => {
        const value = e.target.value;

        setAnswer(value);
        saveAnswer(questionId, value);
    };

    const wordCount = answer
        .trim()
        .split(/\s+/)
        .filter(Boolean).length;

    const characterCount = answer.length;

    return (
        <div
            style={{
                background: "#ffffff",
                padding: "25px",
                borderRadius: "10px",
                boxShadow: "0 4px 10px rgba(0,0,0,0.08)"
            }}
        >
            <label
                style={{
                    display: "block",
                    fontWeight: "600",
                    marginBottom: "12px",
                    fontSize: "18px"
                }}
            >
                Your Answer
            </label>

            <textarea
                rows={10}
                value={answer}
                onChange={handleChange}
                placeholder="Type your answer here..."
                style={{
                    width: "100%",
                    padding: "15px",
                    borderRadius: "8px",
                    border: "1px solid #ccc",
                    resize: "vertical",
                    fontSize: "16px",
                    boxSizing: "border-box",
                    outline: "none"
                }}
            />

            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    marginTop: "12px",
                    fontSize: "14px",
                    color: "#555"
                }}
            >
                <span>Words: {wordCount}</span>

                <span>Characters: {characterCount}</span>
            </div>

            {wordCount < 20 && (
                <p
                    style={{
                        color: "#d97706",
                        marginTop: "10px",
                        fontSize: "14px"
                    }}
                >
                    Try to provide a detailed answer (minimum 20 words recommended).
                </p>
            )}
        </div>
    );
}

export default AnswerBox;