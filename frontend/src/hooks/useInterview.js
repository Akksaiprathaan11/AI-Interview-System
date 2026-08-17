/**
 * Custom Interview Hook
 *
 * Provides easy access to the Interview Context.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

import { useInterviewContext } from "../context/InterviewContext";

const useInterview = () => {
    return useInterviewContext();
};

export default useInterview;