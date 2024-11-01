import argparse
import subprocess

from fasthtml.common import *
from pages.landing import LandingPage

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

### Reload Tailwind CSS, dev only
if args.reload_tailwind:
    subprocess.run(["tailwindcss", "-i", "css/input.css", "-o", "css/output.css"])

### Set head elements
# cnd_tailwind = Script(src="https://cdn.tailwindcss.com")
local_tailwind = Link(rel="stylesheet", href="css/output.css", type="text/css")
favicon = Link(rel="icon", href="/assets/favicon.ico", type="image/x-icon")

### Set up FastHTML app
app, rt = fast_app(
    live=True,
    pico=False,
    hdrs=[
        # cnd_tailwind,
        local_tailwind,
        favicon,
    ],
)


### Set up routes
@rt("/")
def get():
    return Title("collins.data"), LandingPage()


serve()
