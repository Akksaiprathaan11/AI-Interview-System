/**
 * Summary Page
 *
 * Displays the final interview evaluation.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

import { useNavigate } from "react-router-dom";

import SummaryCard from "../components/SummaryCard";
import useInterview from "../hooks/useInterview";

function Summary() {
    const navigate = useNavigate();

    const {
        summary,
        candidate,
        resetInterview,
    } = useInterview();

    const handleNewInterview = () => {
        resetInterview();
        navigate("/");
    };

    return (
        <div
            style={{
                maxWidth: "1000px",
                margin: "40px auto",
                padding: "20px",
            }}
        >
            <h1
                style={{
                    textAlign: "center",
                    color: "#2563eb",
                    marginBottom: "10px",
                }}
            >
                Interview Report
            </h1>

            {candidate && (
                <div
                    style={{
                        background: "#ffffff",
                        padding: "20px",
                        borderRadius: "10px",
                        marginBottom: "30px",
                        boxShadow: "0 4px 12px rgba(0,0,0,0.08)",
                    }}
                >
                    <h3>Candidate Details</h3>

                    <p>
                        <strong>Name:</strong> {candidate.name}
                    </p>

                    <p>
                        <strong>Email:</strong> {candidate.email}
                    </p>

                    <p>
                        <strong>Applied Role:</strong> {candidate.role}
                    </p>
                </div>
            )}

            <SummaryCard summary={summary} />

            <div
                style={{
                    marginTop: "30px",
                    textAlign: "center",
                }}
            >
                <button
                    onClick={handleNewInterview}
                    style={{
                        padding: "12px 30px",
                        backgroundColor: "#2563eb",
                        color: "#ffffff",
                        border: "none",
                        borderRadius: "8px",
                        cursor: "pointer",
                        fontSize: "16px",
                        fontWeight: "600",
                    }}
                >
                    Start New Interview
                </button>
            </div>
        </div>
    );
}

export default Summary;