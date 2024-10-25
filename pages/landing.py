from fasthtml.common import *


def TopBar():
    return Header(
        Div(
            H1(
                "collins",
                Span(".data", cls="text-red-600"),
                cls="text-2xl font-bold text-blueGray-800",
            ),
            P("data scientist & analyst", cls="text-sm text-blueGray-500"),
        ),
        Nav(
            P(
                "Projects",
                href="#",
                cls="text-blueGray-500 hover:text-red-600 transition-colors",
            ),
            P(
                "Publications",
                href="#",
                cls="text-blueGray-500 hover:text-red-600 transition-colors",
            ),
            P(
                "About",
                href="#",
                cls="text-blueGray-500 hover:text-red-600 transition-colors",
            ),
            cls="flex space-x-4",
        ),
        Img(
            src="/assets/unnamed.webp?height=40&width=40",
            alt="Profile",
            width="{40}",
            height="{40}",
            cls="rounded-full",
        ),
        cls="flex justify-between items-center mb-12",
    )


def SubHeader():
    return Div(
        Div(
            H2(
                "Hi, I'm Richard Collins — a data scientist and analyst.",
                cls="text-3xl font-bold mb-4 text-bluegray-800",
            ),
            P(
                "I transform complex data into actionable insights. With expertise in machine learning, statistical analysis, and data visualization, I help organizations make data-driven decisions.",
                cls="text-bluegray-500 mb-6",
            ),
            Div(
                Div(
                    "Barchart",
                    Span("Data Analysis"),
                    cls="flex items-center gap-2 text-red-600",
                ),
                Div(
                    "Piechart",
                    Span("Visualization"),
                    cls="flex items-center gap-2 text-red-900",
                ),
                Div(
                    "Code",
                    Span("Machine Learning"),
                    cls="flex items-center gap-2 text-bluegray-800",
                ),
                cls="flex flex-wrap gap-4 mb-6",
            ),
            cls="relative",
        ),
        cls="mb-16 relative",
    )


def Page():
    return Div(
        Div(
            TopBar(),
            SubHeader(),
            cls="max-w-3xl mx-auto px-4 py-8",
        ),
        cls="min-h-screen bg-gradient-to-br from-orange-100 via-white to-blueGray-500/10",
    )
