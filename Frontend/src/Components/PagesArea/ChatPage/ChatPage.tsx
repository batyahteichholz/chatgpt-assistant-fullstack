import { useState, useRef, useEffect } from "react";
import { ChatMessage } from "../../../Models/ChatMessage";
import { chatService } from "../../../Services/ChatService";
import { notify } from "../../../Utils/Notify";
import "./ChatPage.css";

export function ChatPage() {
    const [messages, setMessages] = useState<ChatMessage[]>([]);
    const [inputValue, setInputValue] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const [conversationId, setConversationId] = useState<number | null>(null);
    const messagesEndRef = useRef<HTMLDivElement>(null);

    // Scroll to bottom when messages update
    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [messages]);

    const handleSendMessage = async () => {
        if (!inputValue.trim() || isLoading) return;

        const userMessage = new ChatMessage("user", inputValue.trim());
        const newMessages = [...messages, userMessage];
        
        setMessages(newMessages);
        setInputValue("");
        setIsLoading(true);

        try {
            const response = await chatService.sendMessage(newMessages, conversationId);
            const assistantMessage = new ChatMessage("assistant", response.message);
            setMessages([...newMessages, assistantMessage]);
            
            // Update conversation ID for subsequent messages
            if (!conversationId) {
                setConversationId(response.conversationId);
            }
        } catch (error: unknown) {
            const message = error instanceof Error ? error.message : "Failed to get response from ChatGPT";
            notify.error(message);
        } finally {
            setIsLoading(false);
        }
    };

    const handleKeyPress = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSendMessage();
        }
    };

    const clearChat = () => {
        setMessages([]);
        setInputValue("");
        setConversationId(null); // Reset conversation ID for new chat
    };

    return (
        <div className="ChatPage">
            <section className="chat-container">
                <div className="chat-header">
                    <div className="chat-title">
                        <h1>Conversation</h1>
                        <p>{conversationId ? `Conversation #${conversationId}` : "Start a new chat"}</p>
                    </div>
                    {messages.length > 0 && (
                        <button className="clear-btn" onClick={clearChat} title="Start a new conversation">
                            New Chat
                        </button>
                    )}
                </div>

                <div className="messages-container">
                    {messages.length === 0 ? (
                        <div className="empty-state">
                            <div className="welcome-message">
                                <h2>Ask anything</h2>
                                <p>Write a message to get started.</p>
                            </div>
                        </div>
                    ) : (
                        messages.map((msg, index) => (
                            <div
                                key={index}
                                className={`message ${msg.role === "user" ? "user-message" : "assistant-message"}`}
                            >
                                <div className="message-avatar">
                                    {msg.role === "user" ? "👤" : "🤖"}
                                </div>
                                <div className="message-content">
                                    <div className="message-role">
                                        {msg.role === "user" ? "You" : "Assistant"}
                                    </div>
                                    <div className="message-text">{msg.content}</div>
                                </div>
                            </div>
                        ))
                    )}
                    {isLoading && (
                        <div className="message assistant-message loading">
                            <div className="message-avatar">🤖</div>
                            <div className="message-content">
                                <div className="message-role">Assistant</div>
                                <div className="typing-indicator">
                                    <span></span>
                                    <span></span>
                                    <span></span>
                                </div>
                            </div>
                        </div>
                    )}
                    <div ref={messagesEndRef} />
                </div>

                <div className="input-container">
                    <textarea
                        value={inputValue}
                        onChange={(e) => setInputValue(e.target.value)}
                        onKeyDown={handleKeyPress}
                        placeholder="Type your message here... (Enter to send, Shift+Enter for new line)"
                        rows={3}
                        disabled={isLoading}
                    />
                    <button
                        onClick={handleSendMessage}
                        disabled={!inputValue.trim() || isLoading}
                        className="send-btn"
                    >
                        {isLoading ? "Sending..." : "Send"}
                    </button>
                </div>
            </section>
        </div>
    );
}
