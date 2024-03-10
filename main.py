from fastapi import FastAPI, Depends, status, HTTPException, Response
from database import engine, get_db 
import schema, model
from routers import history, transactions, users, auth, transactions, admin, vote
from config import settings as ss
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title=ss.project_title, description="Cooperative", version=ss.project_version)

origins = ["https://www.google.com", "https://www.youtube.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(history.router)
app.include_router(transactions.router)
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(vote.router)



model.Base.metadata.create_all(engine)

















 


# if __name__== "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=9000)


