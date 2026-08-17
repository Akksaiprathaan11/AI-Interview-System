/**
 * Interview Page
 *
 * Displays interview questions and collects answers.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import useInterview from "../hooks/useInterview";

import ProgressBar from "../components/ProgressBar";
import QuestionCard from "../components/QuestionCard";
import AnswerBox from "../components/AnswerBox";

import {
    getInterviewQuestions,
    submitAnswer,
    evaluateInterview,
} from "../services/interviewService";

function Interview() {
    const navigate = useNavigate();

    const {
        sessionId,
        questions,
        setQuestions,

        currentQuestion,
        setCurrentQuestion,

        answers,

        setSummary,
        loading,
        setLoading,
    } = useInterview();

    const [submitting, setSubmitting] = useState(false);

    useEffect(() => {
        const loadQuestions = async () => {
            if (!sessionId) return;

            try {
                setLoading(true);

                const response = await getInterviewQuestions(sessionId);

                setQuestions(response.questions || []);
            } catch (error) {
                console.error(error);
            } finally {
                setLoading(false);
            }
        };

        loadQuestions();
    }, [sessionId]);

    const handleNext = async () => {
        const question = questions[currentQuestion];

        if (!question) return;

        const answer = answers[question.id] || "";
        console.log("SESSION ID:", sessionId);
        console.log("QUESTIONS API RESPONSE:", response);
         console.log("QUESTIONS:", response?.questions);

        try {
            setSubmitting(true);

            await submitAnswer({
                session_id: sessionId,
                question_id: question.id,
                answer: answer,
            });

            if (currentQuestion < questions.length - 1) {
                setCurrentQuestion(currentQuestion + 1);
            } else {
                const result = await evaluateInterview(sessionId);

                setSummary(result);

                navigate("/summary");
            }
        } catch (error) {
            console.error(error);
            alert("Failed to submit answer.");
        } finally {
            setSubmitting(false);
        }
    };

    const handlePrevious = () => {
        if (currentQuestion > 0) {
            setCurrentQuestion(currentQuestion - 1);
        }
    };

    if (loading) {
        return (
            <h2 style={{ textAlign: "center", marginTop: "50px" }}>
                Loading Interview...
            </h2>
        );
    }

    return (
        <div
            style={{
                maxWidth: "900px",
                margin: "40px auto",
                padding: "20px",
            }}
        >
            <ProgressBar
                currentQuestion={currentQuestion}
                totalQuestions={questions.length}
            />

            <QuestionCard
                question={questions[currentQuestion]}
                currentQuestion={currentQuestion}
                totalQuestions={questions.length}
            />

            {questions.length > 0 && (
                <AnswerBox
                    questionId={questions[currentQuestion].id}
                />
            )}

            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    marginTop: "30px",
                }}
            >
                <button
                    onClick={handlePrevious}
                    disabled={currentQuestion === 0}
                    style={buttonStyle}
                >
                    Previous
                </button>

                <button
                    onClick={handleNext}
                    disabled={submitting}
                    style={buttonStyle}
                >
                    {currentQuestion === questions.length - 1
                        ? "Finish Interview"
                        : "Next Question"}
                </button>
            </div>
        </div>
    );
}

const buttonStyle = {
    padding: "12px 25px",
    backgroundColor: "#2563eb",
    color: "#ffffff",
    border: "none",
    borderRadius: "6px",
    cursor: "pointer",
    fontSize: "15px",
    fontWeight: "600",
};

export default Interview;