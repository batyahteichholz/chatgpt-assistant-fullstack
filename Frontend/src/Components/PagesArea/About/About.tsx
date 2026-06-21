import "./About.css";

export function About() {
    return (
        <div className="About">
            <div className="about-container">
                <div className="about-header">
                    <h1>About the System</h1>
                    <h2>Architecture and capabilities overview</h2>
                </div>

                <div className="about-content">
                    <section className="system-info">
                        <h3>📋 About the Project</h3>
                        <p>
                            An advanced ChatGPT system that allows users to manage continuous conversations with AI.
                            Conversations are saved to a database and support full conversation continuity.
                        </p>
                    </section>

                    <section className="tech-stack">
                        <h3>🛠️ Technologies</h3>
                        <div className="tech-grid">
                            <div className="tech-item">
                                <strong>Frontend:</strong>
                                <ul>
                                    <li>React 19</li>
                                    <li>TypeScript</li>
                                    <li>Vite</li>
                                    <li>React Router</li>
                                    <li>Axios</li>
                                </ul>
                            </div>
                            <div className="tech-item">
                                <strong>Backend:</strong>
                                <ul>
                                    <li>Python</li>
                                    <li>FastAPI</li>
                                    <li>SQLAlchemy</li>
                                    <li>OpenAI API</li>
                                </ul>
                            </div>
                            <div className="tech-item">
                                <strong>Database:</strong>
                                <ul>
                                    <li>MySQL</li>
                                    <li>Conversation tracking</li>
                                    <li>Message history</li>
                                </ul>
                            </div>
                        </div>
                    </section>

                    <section className="features">
                        <h3>✨ Features</h3>
                        <ul>
                            <li>💬 Continuous conversations with context memory</li>
                            <li>💾 Conversation storage in database</li>
                            <li>🔄 Ability to start new conversations</li>
                            <li>🎨 Aesthetic and user-friendly interface</li>
                            <li>⚡ Fast responses</li>
                            <li>🔒 API key security</li>
                        </ul>
                    </section>

                    <section className="developer-info">
                        <h3>👨‍💻 About the Developer</h3>
                        <p>
                            <strong>Name:</strong> [Developer Name]
                        </p>
                        <p>
                            <strong>Description:</strong> Full Stack Developer specializing in Python and React
                        </p>
                        <p>
                            <strong>Project:</strong> Full Stack Web Developer Project - Database | Python | REST API | React | GenAI
                        </p>
                    </section>

                    <section className="contact-info">
                        <h3>📧 Contact</h3>
                        <p>GitHub: <a href="https://github.com" target="_blank" rel="noopener noreferrer">[Profile Link]</a></p>
                        <p>Email: [Email Address]</p>
                    </section>
                </div>

                <div className="about-footer">
                    <p>© 2026 ChatGPT Assistant | Built with ❤️ using React & Python</p>
                </div>
            </div>
        </div>
    );
}
