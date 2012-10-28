import os
from flask import Flask, render_template, make_response, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("dashboard.html")

@app.route('/data_update', methods=['GET'])
def system_parameters():
    data_type = request.args.get("data")
    if data_type == "system_parameters":
        filename_prefix = "erc_system_parameters_"
    elif data_type == "adequacy":
        filename_prefix = "erc_adequacy_table_"
    elif data_type == "price":
        filename_prefix = "erc_price_graph_"
    elif data_type == "load":
        filename_prefix = "erc_load_graph_"
    elif data_type == "wind":
        filename_prefix = "erc_wind_graph_"
    else:
        raise Exception("Invalid type: %s" %data_type)
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    last_file_name = sorted([f for f in os.listdir(data_dir) if f.startswith(filename_prefix)])[-1]
    response = make_response(
        open(os.path.join(data_dir, last_file_name)).read()
    )
    response.headers["Content-type"] = "text/plain"
    return response


@app.route('/adequacy', methods=['GET'])
def adequacy():
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    last_file_name = sorted([f for f in os.listdir(data_dir) if f.startswith("erc_adequacy_table_")])[-1]
    response = make_response(
        open(os.path.join(data_dir, last_file_name)).read()
    )
    response.headers["Content-type"] = "text/plain"
    return response


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run("0.0.0.0", port, debug=True) #run app
