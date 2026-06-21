class AppConfig {
    public readonly serverUrl = import.meta.env.VITE_SERVER_URL || "http://localhost:4000/api";
}

export const appConfig = new AppConfig(); // Singleton
