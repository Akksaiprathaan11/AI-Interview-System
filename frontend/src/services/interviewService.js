/**
 * Interview Service
 *
 * Handles all interview-related API requests.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

import api from "./api";

/**
 * Start Interview
 *
 * @param {number} candidateId
 * @returns {Promise}
 */
export const startInterview = async (data) => {
    const response = await api.post(
        "/api/interview/start",
        data
    );

    return response.data;
};

/**
 * Get Interview Questions
 *
 * @param {number} sessionId
 * @returns {Promise}
 */
export const getInterviewQuestions = async (sessionId) => {
    const response = await api.get(
        `/api/interview/questions/${sessionId}`
    );

    return response.data;
};

/**
 * Submit Candidate Answer
 *
 * @param {Object} answerData
 * @returns {Promise}
 */
export const submitAnswer = async (answerData) => {
    const response = await api.post(
        "/api/interview/answer",
        answerData
    );

    return response.data;
};

/**
 * Evaluate Interview
 *
 * @param {number} sessionId
 * @returns {Promise}
 */
export const evaluateInterview = async (sessionId) => {
    const response = await api.post(
        "/api/interview/evaluate",
        {
            session_id: sessionId,
        }
    );

    return response.data;
};

/**
 * Get Interview Summary
 *
 * @param {number} sessionId
 * @returns {Promise}
 */
export const getInterviewSummary = async (sessionId) => {
    const response = await api.get(
        `/api/interview/summary/${sessionId}`
    );

    return response.data;
};

/**
 * Get Health Status
 *
 * @returns {Promise}
 */
export const getHealthStatus = async () => {
    const response = await api.get("/api/health");

    return response.data;
};