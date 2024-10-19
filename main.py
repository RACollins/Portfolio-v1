from fasthtml.common import *

app, rt = fast_app()


@rt("/")
def get():
    return Div(
        P("Hello World!"),
        A("Click Me!", hx_get="/change", hx_target="div")
    )


@rt("/change")
def get():
    return Div(
        P("Nice to be here!"),
        A("Go Back!", hx_get="/", hx_target="div")
    )


serve()
