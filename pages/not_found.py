from fasthtml.common import *
from lucide_fasthtml import Lucide


def NotFoundPage():
    return Div(
        Main(
            Div(
                Section(
                    Div(
                        H1(
                            "404: Page Not Found",
                            cls="text-3xl font-bold mb-4 text-darkblue-800 dark:text-gray-200",
                        ),
                        P(
                            "Sorry, looks like this page doesn't exist!",
                            cls="text-darkblue-800 dark:text-gray-300 mb-6",
                        ),
                        A(
                            Lucide(icon="arrow-left"),
                            Span("Go Back Home"),
                            cls="inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-darkblue-800 text-white hover:bg-darkblue-400 dark:bg-gray-700 dark:hover:bg-darkblue-400 transition-colors duration-200",
                            href="/",
                        ),
                        cls="text-center flex flex-col items-center",
                    ),
                    cls="mb-16 relative",
                ),
                cls="max-w-3xl mx-auto px-4",
            ),
            cls="py-8",
        ),
        cls="min-h-screen bg-[radial-gradient(ellipse_at_top_left,_#fff0d1_0%,_#ffffff_60%,_#cce6ff_100%)] dark:bg-[radial-gradient(ellipse_at_top_left,_#003196_0%,_#000000_60%,_#6a3400_100%)] animate-gradientX-top-left",
    )
