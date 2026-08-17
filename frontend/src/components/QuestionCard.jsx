/**
 * QuestionCard Component
 *
 * Displays the current interview question.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

function QuestionCard({
    question,
    currentQuestion,
    totalQuestions
}) {
    if (!question) {
        return (
            <div
                style={{
                    textAlign: "center",
                    marginTop: "40px",
                    color: "#666"
                }}
            >
                No question available.
            </div>
        );
    }

    return (
        <div
            style={{
                background: "#ffffff",
                padding: "30px",
                borderRadius: "12px",
                boxShadow: "0 4px 12px rgba(0,0,0,0.08)",
                marginBottom: "25px"
            }}
        >
            {/* Question Number */}

            <div
                style={{
                    color: "#2563eb",
                    fontWeight: "600",
                    marginBottom: "10px"
                }}
            >
                Question {currentQuestion + 1} of {totalQuestions}
            </div>

            {/* Question */}

            <h2
                style={{
                    fontSize: "22px",
                    lineHeight: "1.6",
                    color: "#1f2937"
                }}
            >
                {question.question}
            </h2>
        </div>
    );
}

export default QuestionCard;