/**
 * RoleSelector Component
 *
 * Allows the candidate to select the
 * interview role.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

function RoleSelector({ value, onChange }) {
    const roles = [
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Data Analyst",
        "Backend Developer",
        "Frontend Developer",
        "Full Stack Developer",
        "Python Developer",
        "Java Developer",
        "Cloud Engineer",
        "DevOps Engineer",
        "Cybersecurity Analyst",
        "SOC Analyst",
        "Network Engineer",
        "Software Engineer",
        "QA Engineer"
    ];

    return (
        <div style={{ marginBottom: "20px" }}>
            <label
                style={{
                    display: "block",
                    marginBottom: "8px",
                    fontWeight: "600",
                }}
            >
                Select Interview Role
            </label>

            <select
                value={value}
                onChange={(e) => onChange(e.target.value)}
                style={{
                    width: "100%",
                    padding: "12px",
                    borderRadius: "6px",
                    border: "1px solid #ccc",
                    fontSize: "15px",
                    background: "#fff",
                }}
            >
                <option value="">Choose Role</option>

                {roles.map((role) => (
                    <option key={role} value={role}>
                        {role}
                    </option>
                ))}
            </select>
        </div>
    );
}

export default RoleSelector;