from fastapi import FastAPI
import uvicorn
from app.routes.bus_routes import router as bus_router

app = FastAPI(title="Oskemen Bus Parser", description="API for Oskemen public transportation schedules")

# Include routers
app.include_router(bus_router)

@app.get("/")
def read_root():
    return {"message": "Oskemen Bus Parser API is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    