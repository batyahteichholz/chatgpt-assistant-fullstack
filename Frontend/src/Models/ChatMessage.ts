export class ChatMessage {
    public role: "user" | "assistant" | "system";
    public content: string;

    public constructor(role: "user" | "assistant" | "system", content: string) {
        this.role = role;
        this.content = content;
    }
}
