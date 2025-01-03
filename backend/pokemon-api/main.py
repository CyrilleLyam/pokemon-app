import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()

def main():
    app_host = os.getenv("APP_HOST")
    app_port = int(os.getenv("APP_PORT"))

    uvicorn.run(
        app="src.server:app",
        host=app_host,
        port=app_port,
        reload=bool(os.getenv("RELOAD", "True").lower() in ["true", "1", "yes"]),
        workers=int(os.getenv("WORKERS", 1))
    )

if __name__ == "__main__":
    main()
