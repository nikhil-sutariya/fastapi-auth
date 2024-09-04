from fastapi import status
from fastapi.responses import JSONResponse

class Response:
    """This class provides a standardized response structure for FastAPI.

    Attributes:
        status (int): The HTTP status code of the response.
        message (str, optional): A user-friendly message describing the response.
        data (dict, list, or None, optional): The actual data returned by the API.
        errors (list[dict], optional): A list of dictionaries containing error details.
    """

    def __init__(self, status: int, message: str = None, data: dict | list | None = None, errors: list[dict] = None):
        self.status = status
        self.message = message
        self.data = data
        self.errors = errors

    @classmethod
    def success(cls, message: str = None, data: dict | list | None = None) -> "Response":
        """Creates a success response.

        Args:
            message (str, optional): A user-friendly message.
            data (dict, list, or None, optional): The actual data.

        Returns:
            Response: A success response object.
        """
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status": status.HTTP_200_OK,
                "message": f"{message}",
                "data": data
            },
        )

    @classmethod
    def created(cls, message: str = None, data: dict | list | None = None) -> "Response":
        """Creates a creation success response.

        Args:
            message (str, optional): A user-friendly message.
            data (dict, list, or None, optional): The actual data.

        Returns:
            Response: A creation success response object.
        """
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "status": status.HTTP_201_CREATED,
                "message": f"{message}",
                "data": data
            },
        )

    @classmethod
    def error(cls, status_code: int, message: str, errors: list[dict] | str = None) -> "Response":
        """Creates an error response.

        Args:
            status_code (int): The HTTP status code of the error.
            message (str): A user-friendly message describing the error.
            errors (list[dict], optional): A list of dictionaries containing error details.

        Returns:
            Response: An error response object.
        """
        return JSONResponse(
            status_code=status_code,
            content={
                "status": status_code,
                "message": f"{message}",
                "error": errors
            },
        )
