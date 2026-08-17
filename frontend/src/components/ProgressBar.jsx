/**
 * ProgressBar Component
 *
 * Displays interview completion progress.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

function ProgressBar({ currentQuestion, totalQuestions }) {
    const progress =
        totalQuestions > 0
            ? ((currentQuestion + 1) / totalQuestions) * 100
            : 0;

    return (
        <div
            style={{
                width: "100%",
                marginBottom: "30px",
            }}
        >
            {/* Header */}

            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    marginBottom: "10px",
                    fontWeight: "600",
                    color: "#374151",
                }}
            >
                <span>
                    Question {currentQuestion + 1} of {totalQuestions}
                </span>

                <span>
                    {Math.round(progress)}%
                </span>
            </div>

            {/* Progress Bar Background */}

            <div
                style={{
                    width: "100%",
                    height: "12px",
                    backgroundColor: "#e5e7eb",
                    borderRadius: "8px",
                    overflow: "hidden",
                }}
            >
                {/* Progress Fill */}

                <div
                    style={{
                        width: `${progress}%`,
                        height: "100%",
                        backgroundColor: "#2563eb",
                        transition: "width 0.4s ease",
                    }}
                />
            </div>
        </div>
    );
}

export default ProgressBar;