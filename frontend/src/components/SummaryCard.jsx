/**
 * SummaryCard Component
 *
 * Displays the final interview evaluation.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

function SummaryCard({ summary }) {
    if (!summary) {
        return (
            <div
                style={{
                    textAlign: "center",
                    marginTop: "40px",
                    color: "#666",
                    fontSize: "18px",
                }}
            >
                No interview summary available.
            </div>
        );
    }

    return (
        <div
            style={{
                maxWidth: "900px",
                margin: "30px auto",
                background: "#ffffff",
                borderRadius: "12px",
                padding: "30px",
                boxShadow: "0 4px 12px rgba(0,0,0,0.08)",
            }}
        >
            <h2
                style={{
                    textAlign: "center",
                    color: "#2563eb",
                    marginBottom: "25px",
                }}
            >
                Interview Summary
            </h2>

            {/* Overall Score */}

            <div
                style={{
                    textAlign: "center",
                    marginBottom: "30px",
                }}
            >
                <h1
                    style={{
                        fontSize: "60px",
                        color: "#16a34a",
                        margin: 0,
                    }}
                >
                    {summary.overall_score ?? 0}%
                </h1>

                <p
                    style={{
                        fontSize: "20px",
                        color: "#555",
                    }}
                >
                    Overall Performance
                </p>
            </div>

            {/* Strengths */}

            <section style={{ marginBottom: "25px" }}>
                <h3 style={{ color: "#2563eb" }}>
                    Strengths
                </h3>

                <ul>
                    {(summary.strengths || []).map((item, index) => (
                        <li key={index}>{item}</li>
                    ))}
                </ul>
            </section>

            {/* Weaknesses */}

            <section style={{ marginBottom: "25px" }}>
                <h3 style={{ color: "#dc2626" }}>
                    Areas for Improvement
                </h3>

                <ul>
                    {(summary.weaknesses || []).map((item, index) => (
                        <li key={index}>{item}</li>
                    ))}
                </ul>
            </section>

            {/* Suggestions */}

            <section style={{ marginBottom: "25px" }}>
                <h3 style={{ color: "#f59e0b" }}>
                    AI Suggestions
                </h3>

                <ul>
                    {(summary.suggestions || []).map((item, index) => (
                        <li key={index}>{item}</li>
                    ))}
                </ul>
            </section>

            {/* Feedback */}

            <section>
                <h3 style={{ color: "#16a34a" }}>
                    Overall Feedback
                </h3>

                <p
                    style={{
                        lineHeight: "1.8",
                        color: "#444",
                    }}
                >
                    {summary.overall_feedback ||
                        "Interview evaluation completed successfully."}
                </p>
            </section>
        </div>
    );
}

export default SummaryCard;