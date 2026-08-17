/**
 * ResumeUploader Component
 *
 * Uploads candidate resume and information.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

import { useState } from "react";
import { uploadResume } from "../services/resumeService";
import useInterview from "../hooks/useInterview";

function ResumeUploader() {
    const { setCandidate } = useInterview();

    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [role, setRole] = useState("");
    const [resume, setResume] = useState(null);

    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!name || !email || !role || !resume) {
            setMessage("Please fill all fields.");
            return;
        }

        const formData = new FormData();

        formData.append("name", name);
        formData.append("email", email);
        formData.append("role", role);
        formData.append("resume", resume);

        try {
            setLoading(true);

            const data = await uploadResume(formData);

            setCandidate(data);

            setMessage("Resume uploaded successfully.");

        } catch (error) {
            console.error(error);
            setMessage("Failed to upload resume.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div
            style={{
                maxWidth: "650px",
                margin: "30px auto",
                padding: "25px",
                background: "#fff",
                borderRadius: "10px",
                boxShadow: "0 0 12px rgba(0,0,0,0.1)"
            }}
        >
            <h2
                style={{
                    textAlign: "center",
                    marginBottom: "20px"
                }}
            >
                Upload Resume
            </h2>

            <form onSubmit={handleSubmit}>

                <input
                    type="text"
                    placeholder="Full Name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    style={inputStyle}
                />

                <input
                    type="email"
                    placeholder="Email Address"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    style={inputStyle}
                />

                <input
                    type="text"
                    placeholder="Job Role (Example: AI Engineer)"
                    value={role}
                    onChange={(e) => setRole(e.target.value)}
                    style={inputStyle}
                />

                <input
                    type="file"
                    accept=".pdf"
                    onChange={(e) => setResume(e.target.files[0])}
                    style={inputStyle}
                />

                <button
                    type="submit"
                    disabled={loading}
                    style={buttonStyle}
                >
                    {loading ? "Uploading..." : "Upload Resume"}
                </button>

            </form>

            {message && (
                <p
                    style={{
                        marginTop: "15px",
                        color: "#2563eb",
                        textAlign: "center",
                        fontWeight: "500"
                    }}
                >
                    {message}
                </p>
            )}
        </div>
    );
}

const inputStyle = {
    width: "100%",
    padding: "12px",
    marginBottom: "15px",
    borderRadius: "6px",
    border: "1px solid #ccc",
    fontSize: "15px",
    boxSizing: "border-box"
};

const buttonStyle = {
    width: "100%",
    padding: "12px",
    backgroundColor: "#2563eb",
    color: "#fff",
    border: "none",
    borderRadius: "6px",
    cursor: "pointer",
    fontSize: "16px",
    fontWeight: "600"
};

export default ResumeUploader;