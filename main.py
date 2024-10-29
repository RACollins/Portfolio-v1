import argparse
import subprocess

from fasthtml.common import *
from pages.landing import Page

### Bring in command line arguments
parser = argparse.ArgumentParser(
    prog="FastHTML + Tailwind Portfolio",
    description="FastHTML app using Tailwind CSS for styling",
)
parser.add_argument(
    "-rt",
    "--reload_tailwind",
    action="store_true",
    help="Run the Tailwind CLI build or not",
)
args = parser.parse_args()

### Set head elements
local_tailwind = Link(rel="stylesheet", href="css/output.css", type="text/css")
favicon = Link(rel="icon", href="/assets/favicon.ico", type="image/x-icon")

### Set up FastHTML app
app, rt = fast_app(
    live=True,
    pico=False,
    hdrs=[
        local_tailwind,
        favicon,
    ],
)


### Set up routes
@rt("/")
def get():
    return Title("collins.data"), Page()


### Reload Tailwind CSS, dev only
if args.reload_tailwind:
    subprocess.run(["./.tailwindcss", "-i", "css/input.css", "-o", "css/output.css"])
serve()
