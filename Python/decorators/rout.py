import os

from absl import app


@app.route("/delete", methods=['POST'])
def delete():
    cmd = "docker container prune -f"

    try:
        os.system(cmd)
        return jsonify({"Status": "Deleted"})
    except:
        return jsonify({"Status": "Not Deleted"})
