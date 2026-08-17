/**
 * Application Routes
 *
 * Defines all routes for the AI Interview System.
 *
 * Author: Akksai Prathaan
 * Project: AI Interview System
 */

import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Interview from "./pages/Interview";
import Summary from "./pages/Summary";
import NotFound from "./pages/NotFound";

function AppRoutes() {
    return (
        <Routes>

            {/* Home */}
            <Route
                path="/"
                element={<Home />}
            />

            {/* Interview */}
            <Route
                path="/interview"
                element={<Interview />}
            />

            {/* Interview Summary */}
            <Route
                path="/summary"
                element={<Summary />}
            />

            {/* 404 Page */}
            <Route
                path="*"
                element={<NotFound />}
            />

        </Routes>
    );
}

export default AppRoutes;