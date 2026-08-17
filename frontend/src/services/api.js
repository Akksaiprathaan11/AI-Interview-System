/**
 * API Configuration
 *
 * Centralized Axios instance for communicating
 * with the FastAPI backend.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

import axios from "axios";

const api = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL,
    timeout: 30000,
    headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
    },
});

/**
 * Request Interceptor
 */
api.interceptors.request.use(
    (config) => {
        return config;
    },
    (error) => Promise.reject(error)
);

/**
 * Response Interceptor
 */
api.interceptors.response.use(
    (response) => response,
    (error) => {
        console.error(
            "API Error:",
            error.response?.data || error.message
        );

        return Promise.reject(error);
    }
);

export default api;