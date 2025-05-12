from fastapi import HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class ErrorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
            return response
        except ValueError as exc:
            return JSONResponse(
                status_code=422,
                content={"error": f"{str(exc)}"}
            )
        except HTTPException as exc:
            return JSONResponse(
                status_code=exc.status_code,
                content={"error": f"{exc.detail}"}
            )
        except Exception:
            return JSONResponse(
                status_code=500,
                content={"message": "Internal server error"}
            )
def error_middleware(func):
    try:
        return func()
    except ValueError as e:
        raise HTTPException(422, detail=str(e), headers={'x-error': str(e)})
    