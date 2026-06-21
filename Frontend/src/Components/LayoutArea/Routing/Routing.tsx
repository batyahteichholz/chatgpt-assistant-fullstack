import { Navigate, Route, Routes } from "react-router-dom";
import { ChatPage } from "../../PagesArea/ChatPage/ChatPage";
import { About } from "../../PagesArea/About/About";
import { Page404 } from "../../PagesArea/Page404/Page404";

export function Routing() {
    return (
        <Routes>
            <Route path="/" element={<Navigate to="/chat" />} />
            <Route path="/chat" element={<ChatPage />} />
            <Route path="/about" element={<About />} />
            <Route path="*" element={<Page404 />} />
        </Routes>
    );
}
