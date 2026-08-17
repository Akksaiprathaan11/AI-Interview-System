/**
 * App Component
 *
 * Root component of the AI Interview System.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

import Navbar from "./components/Navbar";
import AppRoutes from "./routes";

function App() {
    return (
        <>
            <Navbar />

            <main
                style={{
                    minHeight: "90vh",
                    padding: "20px",
                    backgroundColor: "#f5f7fa"
                }}
            >
                <AppRoutes />
            </main>
        </>
    );
}

export default App;