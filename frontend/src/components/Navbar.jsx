/**
 * Navbar Component
 *
 * Displays the navigation bar for the
 * AI Interview System.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

import { NavLink } from "react-router-dom";

function Navbar() {
    const linkStyle = ({ isActive }) => ({
        color: isActive ? "#2563eb" : "#374151",
        textDecoration: "none",
        fontWeight: isActive ? "600" : "500",
        padding: "8px 12px",
        borderRadius: "6px",
        transition: "0.3s",
    });

    return (
        <nav
            style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                padding: "15px 40px",
                background: "#ffffff",
                boxShadow: "0 2px 10px rgba(0,0,0,0.08)",
                position: "sticky",
                top: 0,
                zIndex: 1000,
            }}
        >
            {/* Logo */}

            <div
                style={{
                    fontSize: "24px",
                    fontWeight: "bold",
                    color: "#2563eb",
                }}
            >
                AI Interview System
            </div>

            {/* Navigation Links */}

            <div
                style={{
                    display: "flex",
                    gap: "20px",
                    alignItems: "center",
                }}
            >
                <NavLink
                    to="/"
                    style={linkStyle}
                >
                    Home
                </NavLink>

                <NavLink
                    to="/interview"
                    style={linkStyle}
                >
                    Interview
                </NavLink>

                <NavLink
                    to="/summary"
                    style={linkStyle}
                >
                    Summary
                </NavLink>
            </div>
        </nav>
    );
}

export default Navbar;