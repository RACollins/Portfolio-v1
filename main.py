import argparse
import subprocess
from fasthtml.common import *
from pages.landing import LandingPage
from pages.about import AboutPage
from pages.thought import ThoughtPage
from pages.not_found import NotFoundPage
from components import ChatWidget
from services.chat import ChatService, ChatConfig
from dotenv import load_dotenv

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

### Load environment variables
load_dotenv()

### Initialize chat service
chat_service = ChatService(ChatConfig(max_history=10))

### Set head elements
local_tailwind = Link(rel="stylesheet", href="/css/output.css", type="text/css")
# local_hl_styles = Link(rel="stylesheet", href="/css/hl-styles.css", type="text/css")
favicon = Link(rel="icon", href="/assets/favicon.ico", type="image/x-icon")
dark_mode_js = Script(src="/static/js/dark-mode.js")
# copy_code_js = Script(src="/static/js/copy-code.js")
chat_js = Script(src="/static/js/chat.js")

# Define exception handlers for 404 errors
exception_handlers = {404: lambda req, exc: NotFoundPage()}

### Set up FastHTML app
app, rt = fast_app(
    exception_handlers=exception_handlers,
    live=True,
    pico=False,
    hdrs=[
        local_tailwind,
        # local_hl_styles,
        favicon,
        MarkdownJS(),
        HighlightJS(
            langs=["python"],
            light="gradient-dark",
            dark="tomorrow-night-blue",
        ),
        dark_mode_js,
        # copy_code_js,
        chat_js,
    ],
)


### Add chat route
@rt("/api/chat", methods=["POST"])
async def post(req):
    form_data = await req.form()
    user_message = form_data.get("chat-input", "")

    # Get response from chat service
    bot_response = await chat_service.get_response(user_message)

    # Return both user message and bot response
    return Div(
        # User message
        Div(
            P(
                user_message,
                cls="bg-blue-100 dark:bg-blue-900 p-3 ml-4 rounded-lg inline-block text-darkblue-800 dark:text-gray-300",
            ),
            cls="flex justify-end mb-4",
        ),
        # Bot response
        Div(
            P(
                bot_response,
                cls="bg-orange-100 dark:bg-amber-900 p-3 mr-4 rounded-lg inline-block text-darkblue-800 dark:text-gray-300",
            ),
            cls="flex justify-start",
        ),
    )


### Set up routes
@rt("/")
def get():
    return (Title("Landing Page Title"), Container(LandingPage()))


@rt("/about")
def get():
    return (Title("About Page Title"), Container(AboutPage()))


@rt("/thoughts/{slug}")
def get(slug: str):
    return (Title(f"Thoughts on {slug}"), Container(ThoughtPage(slug)))


@rt("/cv.pdf")
def get():
    try:
        return FileResponse("static/cv.pdf")
    except:
        return (Title("404 - Not Found"), Container(NotFoundPage()))


# This should be the last route - it catches all unmatched paths
@rt("/{path:path}")
def get(path: str):
    return (Title("404 - Not Found"), Container(NotFoundPage()))


serve()
