import { Notyf } from "notyf"; // npm i notyf

class Notify {

    private notyf = new Notyf({
        position: { x: "center", y: "top" },
        duration: 3000,
        dismissible: true,
        ripple: true // Ripple = אדווה = גל קטן
    });

    public error(err: unknown): void {
        const message = this.extractErrorMessage(err);
        this.notyf.error(message);
    }

    private extractErrorMessage(err: unknown): string {
        if(typeof err === "string") return err; // String error.
        
        if (typeof err === "object" && err !== null) {
            const asError = err as { response?: { data?: unknown }; message?: unknown };
            if (typeof asError.response?.data === "string") return asError.response.data; // Axios error

            if (
                typeof asError.response?.data === "object" &&
                asError.response.data !== null &&
                "message" in asError.response.data
            ) {
                const responseData = asError.response.data as { message?: unknown };
                if (typeof responseData.message === "string") return responseData.message;
            }

            if (typeof asError.message === "string") return asError.message; // throw new Error("...")
        }

        return "Some error, please try again.";
    }

}

export const notify = new Notify();
