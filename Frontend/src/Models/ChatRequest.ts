export class ChatRequest {
    public messages: Array<{ role: string; content: string }>;
    public conversation_id?: number | null;
    public model?: string;
    public temperature?: number;

    public constructor(
        messages: Array<{ role: string; content: string }>,
        conversation_id: number | null = null,
        model: string = "gpt-4o-mini",
        temperature: number = 0.7
    ) {
        this.messages = messages;
        this.conversation_id = conversation_id;
        this.model = model;
        this.temperature = temperature;
    }
}
