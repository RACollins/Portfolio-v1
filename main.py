import argparse
import subprocess

from fasthtml.common import *
from pages.landing import LandingPage
from pages.about import AboutPage
from pages.thought import ThoughtPage
from pages.not_found import NotFoundPage
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
    subprocess.run(
        ["tailwindcss", "-i", "css/input.css", "-o", "css/output.css", "--minify"]
    )

### Set head elements
local_tailwind = Link(rel="stylesheet", href="/css/output.css", type="text/css")
local_hl_styles = Link(rel="stylesheet", href="/css/hl-styles.css", type="text/css")
favicon = Link(rel="icon", href="/assets/favicon.ico", type="image/x-icon")
dark_mode_js = Script(src="/static/js/dark-mode.js")
copy_code_js = Script(src="/static/js/copy-code.js")

# Define exception handlers for 404 errors
exception_handlers = {
    404: lambda req, exc: NotFoundPage()
}

### Set up FastHTML app
app, rt = fast_app(
    exception_handlers=exception_handlers,
    live=True,
    pico=False,
    hdrs=[
        local_tailwind,
        local_hl_styles,
        favicon,
        dark_mode_js,
        copy_code_js,
    ],
)

### Serve static files for dark mode toggle, but seems like I don't need it?
""" @rt("/{fname:path}.{ext:static}")
async def get(fname: str, ext: str):
    return FileResponse(f'static/{fname}.{ext}') """


### Set up routes
@rt("/")
def get():
    return LandingPage()


@rt("/about")
def get():
    return AboutPage()


@rt("/thoughts/{slug}")
def get(slug: str):
    return ThoughtPage(slug)

@rt("/cv.pdf")
def get():
    try:
        return FileResponse("static/cv.pdf")
    except:
        return NotFoundPage()

# This should be the last route - it catches all unmatched paths
@rt("/{path:path}")
def get(path: str):
    return NotFoundPage()

serve()
