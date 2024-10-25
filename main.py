from fasthtml.common import *
from pages.landing import Page

tailwind = Script(src="https://cdn.tailwindcss.com")
app, rt = fast_app(live=True, pico=False, hdrs=[tailwind])

@rt("/")
def get():
    return Page()

serve()
