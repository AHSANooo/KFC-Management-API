# main.py

from fastapi.middleware.cors import CORSMiddleware
from api.auth.endpoints import router as auth_router
from api.products.endpoints import router as products_router
from api.orders.endpoints import router as orders_router
from api.inventory.endpoints import router as inventory_router
from src.utils.logger import Logger
from src.database import init_db
from fastapi import FastAPI

# Setup logger
logger = Logger.setup_logger("app", "app.log")

# Create FastAPI app
app = FastAPI()

init_db()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(products_router, prefix="/products", tags=["products"])
app.include_router(orders_router, prefix="/orders", tags=["orders"])
app.include_router(inventory_router, prefix="/inventory", tags=["inventory"])

# Root endpoint
@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the KFC Management System"}

# Exception handling for validation errors
@app.exception_handler(Exception)
async def validation_exception_handler(request, exc):
    logger.error(f"Unexpected error: {exc}")
    return {"detail": str(exc)}

if __name__ == "__main__":
    import uvicorn

    logger.info("Starting the FastAPI application")
    uvicorn.run(app, host="0.0.0.0", port=8000)
