/**
 * Resume Service
 *
 * Handles all resume-related API requests.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

import api from "./api";

/**
 * Upload Resume
 *
 * @param {FormData} formData
 * @returns {Promise}
 */
export const uploadResume = async (formData) => {
    const response = await api.post(
        "/api/resume/upload",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
};

/**
 * Get Candidate by ID
 *
 * @param {number} candidateId
 * @returns {Promise}
 */
export const getCandidate = async (candidateId) => {
    const response = await api.get(
        `/api/resume/${candidateId}`
    );

    return response.data;
};

/**
 * Get All Candidates
 *
 * @returns {Promise}
 */
export const getAllCandidates = async () => {
    const response = await api.get(
        "/api/resume/"
    );

    return response.data;
};