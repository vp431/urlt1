from flask import Blueprint, render_template, request
from .limiter import limiter

api = Blueprint("api", __name__)


@api.route("/api", methods=["GET"])
@limiter.exempt
def api_route():
    return render_template("api.html", host_url=request.host_url)
