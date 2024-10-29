from fasthtml.common import *

tailwind = Script(src="https://cdn.tailwindcss.com")
app, rt = fast_app(live=True, pico=False, hdrs=[tailwind])

def with_card(colour: str, border_colour: str, padding: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            content = func(*args, **kwargs)
            tailwind_classes = f"p-{padding} rounded-lg shadow-lg bg-{colour}-100 border border-{border_colour}-500"
            return Div(
                Div(content, cls=tailwind_classes),
                cls=f"card border border-{border_colour}-500 shadow-lg rounded-lg m-4",
            )

        return wrapper

    return decorator


@with_card(colour="lightblue", border_colour="blue", padding="10")
def Card(title: str, description: str, another_description: str):
    return Div(H1(title), P(description), P(another_description))


@rt("/")
def get():
    return Titled(
        Div(P("Hello World!"), A("Click Me!", hx_get="/change", hx_target="div"))
    )


@rt("/change")
def get():
    return Div(
        P("Nice to be here!"),
        A("Go Back!", hx_get="/", hx_target="div"),
        Card(
            title="Title",
            description="Description",
            another_description="Another description",
        ),
    )