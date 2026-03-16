def rest_bean(code, message, data):
    return {
        "code": code,
        "message": message,
        "data": data
    }
        
class RestBean:
    @classmethod
    def success(cls, data):
        return rest_bean(200, "success", data)

    @classmethod
    def error(cls, message):
        return rest_bean(500, message, None)

    @classmethod
    def notFound(cls):
        return rest_bean(404, "resource not found", None)

    @classmethod
    def unauthorized(cls):
        return rest_bean(401, "unauthorized", None)

    @classmethod
    def forbidden(cls):
        return rest_bean(403, "forbidden", None)

    @classmethod
    def badRequest(cls):
        return rest_bean(400, "bad request", None)