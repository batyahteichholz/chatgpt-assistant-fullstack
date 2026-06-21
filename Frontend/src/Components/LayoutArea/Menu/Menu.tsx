import { NavLink } from "react-router-dom";
import "./Menu.css";

export function Menu() {
    return (
        <div className="Menu">
            <NavLink to="/chat" className={({ isActive }) => isActive ? "menu-link active" : "menu-link"}>
                Chat
            </NavLink>
            <NavLink to="/about" className={({ isActive }) => isActive ? "menu-link active" : "menu-link"}>
                About
            </NavLink>
        </div>
    );
}
