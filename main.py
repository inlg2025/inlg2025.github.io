# pylint: disable=global-statement,redefined-outer-name
import argparse
import csv
import glob
import json
import os
import re
from datetime import datetime

import yaml
from flask import Flask, jsonify, redirect, render_template, send_from_directory
from flask_frozen import Freezer
from flaskext.markdown import Markdown

site_data = {}
by_uid = {}
by_date = {}


def load_sitedata(site_data_path):
    global site_data, extra_files
    extra_files = []
    # Load all for your sitedata one time.
    for f in glob.glob(site_data_path + "/*"):
        print(f)
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
markdown = Markdown(app)


# MAIN PAGES
def _data():
    data = {}
    data["config"] = site_data["config"]
    return data


@app.route("/")
def index():
    return redirect("/index.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(site_data_path, "favicon.ico")


# TOP LEVEL PAGES
@app.route("/index.html")
def home():
    data = _data()
    data["home"] = open("sitedata/Home.md").read()
    return render_template("index.html", **data)


def extract_list_field(v, key):
    value = v.get(key, "")
    if isinstance(value, list):
        return value
    else:
        return value.split("|")


def format_paper(v):
    v["authors"] = extract_list_field(v, "authors")
    dt = datetime.strptime(v["start_time"], "%Y-%m-%dT%H:%M:%SZ")
    v["time"] = dt.strftime("%A %m/%d %H:%M EST")
    v["short_time"] = dt.strftime("%H:%M EST")
    v["title"] = v["title"].title()
    v["title"] = re.sub(r"Nlg", "NLG", v["title"])
    return v


def format_workshop(v):
    v["organizers"] = extract_list_field(v, "authors")
    dt = datetime.strptime(v["start_time"], "%Y-%m-%dT%H:%M:%SZ")
    v["time"] = dt.strftime("%A %m/%d %H:%M EST")
    return v


# ITEM PAGES
@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)


# --------------- DRIVER CODE -------------------------->
# Code to turn it all static


@freezer.register_generator
def generator():
    for paper in site_data["papers"]:
        yield "poster", {"poster": str(paper["UID"])}

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

        app.run(port=5000, debug=debug_val, extra_files=extra_files)
