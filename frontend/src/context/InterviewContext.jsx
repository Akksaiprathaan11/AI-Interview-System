/**
 * Interview Context
 *
 * Provides global state management for the
 * AI Interview System.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

import { createContext, useContext, useState } from "react";

const InterviewContext = createContext();

export const InterviewProvider = ({ children }) => {
    // Candidate Information
    const [candidate, setCandidate] = useState(null);

    // Interview Session
    const [sessionId, setSessionId] = useState(null);

    // Interview Questions
    const [questions, setQuestions] = useState([]);

    // Current Question Index
    const [currentQuestion, setCurrentQuestion] = useState(0);

    // Candidate Answers
    const [answers, setAnswers] = useState({});

    // Interview Summary
    const [summary, setSummary] = useState(null);

    // Loading State
    const [loading, setLoading] = useState(false);

    /**
     * Save an Answer
     */
    const saveAnswer = (questionId, answer) => {
        setAnswers((prev) => ({
            ...prev,
            [questionId]: answer,
        }));
    };

    /**
     * Reset Interview
     */
    const resetInterview = () => {
        setCandidate(null);
        setSessionId(null);
        setQuestions([]);
        setCurrentQuestion(0);
        setAnswers({});
        setSummary(null);
        setLoading(false);
    };

    return (
        <InterviewContext.Provider
            value={{
                candidate,
                setCandidate,

                sessionId,
                setSessionId,

                questions,
                setQuestions,

                currentQuestion,
                setCurrentQuestion,

                answers,
                saveAnswer,

                summary,
                setSummary,

                loading,
                setLoading,

                resetInterview,
            }}
        >
            {children}
        </InterviewContext.Provider>
    );
};

/**
 * Custom Hook
 */
export const useInterviewContext = () => {
    return useContext(InterviewContext);
};