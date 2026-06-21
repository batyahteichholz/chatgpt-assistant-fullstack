from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.chat_controller import router as chat_router
from uvicorn import run
from middleware.exception_handler import register_exception_handlers
from middleware.logger_middleware import LoggerMiddleware
from utils.app_config import AppConfig

# Create the main server:
server = FastAPI()

# Register exception handlers: 
register_exception_handlers(server)

# Add CORS middleware to allow frontend communication
server.add_middleware(
    CORSMiddleware,
    allow_origins=[AppConfig.frontend_origin],
    allow_origin_regex=r"https?://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register middleware: 
server.add_middleware(LoggerMiddleware)

# Register routes: 
server.include_router(chat_router)

# Run server: 
if __name__ == "__main__":
    print("🚀 Starting FastAPI server on http://localhost:4000")
    print("📊 Check API docs at http://localhost:4000/docs")
    run("app:server", host="127.0.0.1", port=4000, reload=True, access_log=True, log_level="info")
