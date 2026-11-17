import streamlit as st
from starlette.routing import Route
from starlette.responses import PlainTextResponse, JSONResponse

async def set_cookie(request):
    response = PlainTextResponse("Cookie criado.")
    response.set_cookie(
        key="vq_probe",
        value="httponly-test-12345",
        max_age=1800,
        httponly=True,
        secure=True,
        samesite="strict",
        path="/"
    )
    return response

async def read_cookie(request):
    value = request.cookies.get("vq_probe")
    return JSONResponse({
        "cookie_received": value is not None,
        "value": value
    })

async def delete_cookie(request):
    response = PlainTextResponse("Cookie eliminado.")
    response.delete_cookie(
        key="vq_probe",
        path="/",
        secure=True,
        httponly=True,
        samesite="strict"
    )
    return response

app = st.App(
    "ui.py",
    routes=[
        Route("/probe/set", set_cookie),
        Route("/probe/read", read_cookie),
        Route("/probe/delete", delete_cookie)
    ]
)

if __name__ == "__main__":
    app.run()
