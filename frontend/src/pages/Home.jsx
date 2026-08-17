/**
 * Home Page
 *
 * Landing page for the AI Interview System.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

import { useNavigate } from "react-router-dom";

import ResumeUploader from "../components/ResumeUploader";
import useInterview from "../hooks/useInterview";
import { startInterview } from "../services/interviewService";

function Home() {
    const navigate = useNavigate();

    const {
        candidate,
        setSessionId,
        setLoading,
    } = useInterview();

    const handleStartInterview = async () => {
        if (!candidate) {
            alert("Please upload your resume first.");
            return;
        }

        try {
            setLoading(true);
            console.log("Candidate:", candidate);
console.log("Candidate ID:", candidate.id);
console.log("Candidate Candidate ID:", candidate.candidate_id);

const candidateId = candidate.id ?? candidate.candidate_id;

if (!candidateId) {
    console.error("Candidate ID is missing:", candidate);
    alert("Candidate ID is missing. Please upload the resume again.");
    return;
}const response = await startInterview({
    candidate_id: candidateId
});

console.log("Start Interview Response:", response);
        console.log("Start Interview Response:", response);
        setSessionId(response.session_id);
        navigate("/interview");
        }
        catch (error) {
            console.error(error);

            alert("Unable to start interview.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div
            style={{
                maxWidth: "900px",
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
                AI Interview System
            </h1>

            <p
                style={{
                    textAlign: "center",
                    color: "#555",
                    marginBottom: "30px",
                    fontSize: "18px",
                }}
            >
                Upload your resume and begin your AI-powered technical interview.
            </p>

            <ResumeUploader />

            {candidate && (
                <div
                    style={{
                        marginTop: "30px",
                        padding: "20px",
                        background: "#ffffff",
                        borderRadius: "10px",
                        boxShadow: "0 4px 10px rgba(0,0,0,0.08)",
                    }}
                >
                    <h3>Candidate Information</h3>

                    <p>
                        <strong>Name:</strong> {candidate.name}
                    </p>

                    <p>
                        <strong>Email:</strong> {candidate.email}
                    </p>

                    <p>
                        <strong>Role:</strong> {candidate.role}
                    </p>

                    <button
                        onClick={handleStartInterview}
                        style={{
                            marginTop: "15px",
                            width: "100%",
                            padding: "12px",
                            backgroundColor: "#2563eb",
                            color: "#ffffff",
                            border: "none",
                            borderRadius: "8px",
                            cursor: "pointer",
                            fontSize: "16px",
                            fontWeight: "600",
                        }}
                    >
                        Start Interview
                    </button>
                </div>
            )}
        </div>
    );
}

export default Home;