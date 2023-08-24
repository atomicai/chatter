import os
from pathlib import Path

from flask import Flask, Response, render_template, request
from gevent import monkey
from rethinkdb import r

from flask_session import Session

monkey.patch_all()
import dotenv

dotenv.load_dotenv()


client = r.connect(host="localhost", port=28015)


app = Flask(
    __name__,
    template_folder="build",
    static_folder="build",
    root_path=Path(os.getcwd()) / "chatter",
)
app.config["SECRET_KEY"] = "deshibasara"

app.config["CELERY_BROKER_URL"] = "amqp://justatom:fate@localhost:5672"
app.config["CELERY_RESULT_BACKEND"] = "redis://localhost:6379/0"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

if os.environ["TABLE"] not in r.table_list().run(client):
    r.table_create(os.environ["TABLE"]).run(client)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/write")
def save_data():
    data = request.args["data"]

    r.table(os.environ["TABLE"]).insert({"data": data}).run(client)
    return "success"


@app.route("/read")
def live_data():
    print(f'live streaming on {os.environ["TABLE"]} table')

    def stream():
        try:
            r.connect("localhost", 28015).repl()
            cursor = r.table(os.environ["TABLE"]).changes().run()
            for document in cursor:
                print(document)
                yield "data:" + str(document["new_val"]["data"]).replace("'", '"') + "\n\n"
        except:
            pass

    return Response(response=stream(), status=200, mimetype="text/event-stream")
