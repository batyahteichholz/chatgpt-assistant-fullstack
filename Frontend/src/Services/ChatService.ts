import axios from "axios";
import { ChatMessage } from "../Models/ChatMessage";
import { ChatRequest } from "../Models/ChatRequest";
import { appConfig } from "../Utils/AppConfig";

class ChatService {
    private readonly baseUrl = `${appConfig.serverUrl}/chat`;

    // Send a message to ChatGPT
    public async sendMessage(messages: ChatMessage[], conversationId: number | null = null): Promise<{ message: string; conversationId: number }> {
        try {
            const request = new ChatRequest(
                messages.map(m => ({ role: m.role, content: m.content })),
                conversationId
            );
            
            const response = await axios.post(`${this.baseUrl}/message`, request);
            return {
                message: response.data.message,
                conversationId: response.data.conversation_id
            };
        } catch (error: any) {
            console.error("Error sending message:", error);
            const responseData = error?.response?.data;
            const apiMessage =
                responseData?.detail ||
                responseData?.message ||
                (typeof responseData === "string" ? responseData : "");

            throw new Error(apiMessage || error?.message || "Failed to send message");
        }
    }

}

export const chatService = new ChatService();
