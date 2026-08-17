/**
 * NotFound Page
 *
 * Displays a 404 page for invalid routes.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

import { Link } from "react-router-dom";

function NotFound() {
    return (
        <div
            style={{
                minHeight: "80vh",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                backgroundColor: "#f5f7fa",
            }}
        >
            <div
                style={{
                    textAlign: "center",
                    background: "#ffffff",
                    padding: "50px",
                    borderRadius: "12px",
                    boxShadow: "0 4px 12px rgba(0,0,0,0.08)",
                    maxWidth: "500px",
                }}
            >
                <h1
                    style={{
                        fontSize: "90px",
                        color: "#2563eb",
                        margin: 0,
                    }}
                >
                    404
                </h1>

                <h2
                    style={{
                        color: "#1f2937",
                        marginTop: "10px",
                    }}
                >
                    Page Not Found
                </h2>

                <p
                    style={{
                        color: "#6b7280",
                        marginBottom: "30px",
                        lineHeight: "1.6",
                    }}
                >
                    The page you are looking for doesn't exist or has been
                    moved.
                </p>

                <Link
                    to="/"
                    style={{
                        display: "inline-block",
                        padding: "12px 25px",
                        backgroundColor: "#2563eb",
                        color: "#ffffff",
                        textDecoration: "none",
                        borderRadius: "8px",
                        fontWeight: "600",
                    }}
                >
                    Go to Home
                </Link>
            </div>
        </div>
    );
}

export default NotFound;