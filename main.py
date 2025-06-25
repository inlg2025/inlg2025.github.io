# pylint: disable=global-statement,redefined-outer-name
import argparse
import csv
import glob
import json
import os

import markdown as md
import yaml
from flask import Flask, jsonify, render_template, send_from_directory
from flask_frozen import Freezer
from markupsafe import Markup

site_data = {}
by_uid = {}
by_date = {}


def load_sitedata(site_data_path):
    global site_data, extra_files
    extra_files = []
    # Load all for your sitedata one time.
    for f in glob.glob(site_data_path + "/*"):
        extra_files.append(f)
        name, typ = f.split("/")[-1].split(".")
        if typ == "json":
            site_data[name] = json.load(open(f))
        elif typ in {"csv", "tsv"}:
            site_data[name] = list(csv.DictReader(open(f)))
        elif typ == "yml":
            site_data[name] = yaml.load(open(f).read(), Loader=yaml.SafeLoader)

    print("Data Successfully Loaded")
    return extra_files


# ------------- SERVER CODE -------------------->

app = Flask(__name__)
app.config.from_object(__name__)
freezer = Freezer(app)


@app.template_filter("markdown")
def filter_markdown(s: str):
    return Markup(md.markdown(s, extensions=["tables"]))


# MAIN PAGES
def _data():
    data = {}
    data["config"] = site_data["config"]
    return data


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(site_data_path, "favicon.ico")


@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory(site_data_path, "sitemap.xml")


# TOP LEVEL PAGES
@app.route("/")
def home():
    data = _data()
    data["gold_sponsors"] = site_data["sponsors"]["gold_sponsors"]
    data["silver_sponsors"] = site_data["sponsors"]["silver_sponsors"]
    data["bronze_sponsors"] = site_data["sponsors"]["bronze_sponsors"]
    data["home"] = open("sitedata/Home.md").read()
    return render_template("index.html", **data)


@app.route("/calls.html")
def calls():
    data = _data()
    data["calls"] = site_data["calls"]["calls"]
    for call in data["calls"]:
        call["bodytext"] = open(call["body"]).read()
    return render_template("calls.html", **data)


@app.route("/registration.html")
def registration():
    data = _data()
    data["mdcontent"] = open("sitedata/registration.md").read()
    data["section_title"] = "Registration"
    return render_template("single_md.html", **data)


@app.route("/banquet.html")
def banquet():
    data = _data()
    data["mdcontent"] = open("sitedata/banquet.md").read()
    data["section_title"] = "Banquet"
    return render_template("single_md.html", **data)


@app.route("/local-info.html")
def local_info():
    data = _data()
    data["mdcontent"] = open("sitedata/local_info.md").read()
    data["section_title"] = "Local Information"
    return render_template("single_md.html", **data)


@app.route("/organizers.html")
def organizers():
    data = _data()
    data['committee'] = site_data["committee"]
    return render_template("organizers.html", **data)


@app.route("/faq.html")
def faq():
    data = _data()
    data["faq"] = site_data["faq"]["faq"]
    return render_template("faq.html", **data)


@app.route("/resource-statement.html")
def resource_statement():
    data = _data()
    data["mdcontent"] = open("sitedata/resource_statement.md").read()
    return render_template("single_md.html", **data)


@app.route("/sponsor-vi.html")
def sponsor_vi():
    data = _data()
    data["mdcontent"] = open("sitedata/sponsor_vi.md").read()
    return render_template("single_md.html", **data)


@app.route("/program.html")
def program():
    data = _data()
    data["mdcontent"] = open("sitedata/program.md").read()
    data["section_title"] = "Program"
    return render_template("single_md.html", **data)


@app.route("/awards.html")
def awards():
    data = _data()
    data["mdcontent"] = open("sitedata/awards.md").read()
    data["section_title"] = "Awards"
    return render_template("single_md.html", **data)


@app.route("/workshops-tutorials.html")
def tutorials():
    data = _data()
    data["calls"] = site_data["tutorials"]["tutorials"]
    for tutorial in data["calls"]:
        if "body" in tutorial:
            tutorial["bodytext"] = open(tutorial["body"]).read()
    return render_template("tutorials.html", **data)


@app.route("/accepted-papers.html")
def accepted_papers():
    data = _data()
    data["mdcontent"] = open("sitedata/accepted_papers.md").read()
    data["section_title"] = "Accepted Papers"
    return render_template("single_md.html", **data)


@app.route("/keynotes.html")
def keynotes():
    data = _data()
    data["mdcontent"] = open("sitedata/keynotes.md").read()
    data["section_title"] = "Keynotes"
    return render_template("single_md.html", **data)


# ITEM PAGES
@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)


@app.route("/serve_<path>.json")
def serve(path):
    return jsonify(site_data[path])

@app.route("/googlee49d4a21699e49c6.html")
def google_ownership(path):
    return send_from_directory(".", path)


# --------------- DRIVER CODE -------------------------->
# Code to turn it all static


@freezer.register_generator
def generator():
    for key in site_data:
        yield "serve", {"path": key}


def parse_arguments():
    parser = argparse.ArgumentParser(description="MiniConf Portal Command Line")

    parser.add_argument(
        "--build",
        action="store_true",
        default=False,
        help="Convert the site to static assets",
    )

    parser.add_argument(
        "-b",
        action="store_true",
        default=False,
        dest="build",
        help="Convert the site to static assets",
    )

    parser.add_argument("path", help="Pass the JSON data path and run the server")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()

    site_data_path = args.path
    extra_files = load_sitedata(site_data_path)

    if args.build:
        freezer.freeze()
    else:
        debug_val = False
        if os.getenv("FLASK_DEBUG") == "True":
            debug_val = True

        app.run(port=8888, debug=debug_val, extra_files=extra_files)
