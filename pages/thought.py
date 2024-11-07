from fasthtml.common import *
from components import TopBar
import yaml
import datetime
from markdown import markdown

# Ensure the extensions are correctly specified
md_exts = ["codehilite", "smarty", "extra", "sane_lists"]

def Markdown(s, exts=md_exts, **kw):
    return Div(NotStr(markdown(s, extensions=exts)), **kw)


def ThoughtPage(slug: str):
    with open(f"thoughts/{slug}.md", "r") as file:
        content = file.read()
        header_info, thought_body = content.split("---")[1:]

        ### Populate thought with metadata
        thought = yaml.safe_load(header_info)
        thought["body"] = thought_body.strip()

        ### Convert date string to datetime object if it exists
        if "date" in thought and isinstance(thought["date"], str):
            thought["date"] = datetime.datetime.strptime(thought["date"], "%Y-%m-%d")

    return Div(
        TopBar(),
        Main(
            H2(
                thought["title"],
                cls="max-w-3xl mx-auto px-4 mb-4 text-3xl font-bold text-darkblue-800 dark:text-sgray-200",
            ),
            H3(
                thought["date"].strftime("%Y-%m-%d"),
                cls="max-w-3xl mx-auto px-4 mb-4 text-lg text-darkblue-600 dark:text-gray-400",
            ),
            Markdown(
                thought["body"],
                cls="max-w-3xl mx-auto px-4 mb-4 text-darkblue-800 dark:text-gray-200",
            ),
            cls="py-8",
        ),
        cls="min-h-screen bg-[radial-gradient(ellipse_at_top_left,_#fff0d1_0%,_#ffffff_60%,_#cce6ff_100%)] dark:bg-[radial-gradient(ellipse_at_top_left,_#003196_0%,_#000000_60%,_#6a3400_100%)] animate-gradientX-top-left",
    )
