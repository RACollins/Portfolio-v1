from fasthtml.common import *
from components import ProjectCard, TopBar
from lucide_fasthtml import Lucide


def SubHeader():
    return Section(
        Div(
            H2(
                "Hi, I'm Richard Collins — a data scientist and analyst.",
                cls="text-3xl font-bold mb-4 text-darkblue-800 dark:text-gray-200",
            ),
            P(
                "I transform complex data into actionable insights. With expertise in machine learning, statistical analysis, and data visualization, I help organisations make data-driven decisions.",
                cls="text-darkblue-800 dark:text-gray-300 mb-6",
            ),
            Div(
                Div(
                    Lucide(icon="file-text"),
                    Span("CV"),
                    cls="flex items-center gap-2 text-slate hover:text-red-400 dark:text-gray-300 dark:hover:text-red-400 transition-colors",
                ),
                Div(
                    Lucide(icon="github"),
                    Span("GitHub"),
                    cls="flex items-center gap-2 text-darkblue-800 hover:text-red-400 dark:text-gray-300 dark:hover:text-red-400 transition-colors",
                ),
                Div(
                    Lucide(icon="linkedin"),
                    Span("LinkedIn"),
                    cls="flex items-center gap-2 text-darkblue-800 hover:text-red-400 dark:text-gray-300 dark:hover:text-red-400 transition-colors",
                ),
                cls="flex flex-wrap gap-4 mb-6",
            ),
            cls="relative",
        ),
        cls="mb-16 relative",
    )


def FeaturedProjects():
    return Section(
        H2("Featured Projects", cls="text-xl font-semibold mb-6 text-darkblue-800 dark:text-gray-200"),
        Div(
            Div(
                ProjectCard(
                    Lucide(icon="audio-waveform"),
                    "Project 1",
                    "This is a description of Project 1",
                    "/projects/1",
                ),
                ProjectCard(
                    Lucide(icon="chart-column-increasing"),
                    "Project 2",
                    "This is a description of Project 2",
                    "/projects/2",
                ),
                cls="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-4 text-darkblue-800 dark:text-gray-200",
            ),
            Div(
                ProjectCard(
                    Lucide(icon="chart-network"),
                    "Project 3",
                    "This is a description of Project 3",
                    "/projects/3",
                ),
                ProjectCard(
                    Lucide(icon="cloud-snow"),
                    "Project 4",
                    "This is a description of Project 4",
                    "/projects/4",
                ),
                cls="grid grid-cols-1 sm:grid-cols-2 gap-4 text-darkblue-800 dark:text-gray-200",
            ),
            cls="max-w-4xl mx-auto",
        ),
        cls="mb-16",
    )


def LandingPage():
    return Div(
        TopBar(),
        Main(
            Div(
                SubHeader(),
                FeaturedProjects(),
                cls="max-w-3xl mx-auto px-4",
            ),
            cls="py-8",
        ),
        cls="min-h-screen bg-[radial-gradient(ellipse_at_top_left,_#fff0d1_0%,_#ffffff_60%,_#cce6ff_100%)] dark:bg-[radial-gradient(ellipse_at_top_left,_#003196_0%,_#000000_60%,_#6a3400_100%)] animate-gradientX-top-left",
    )
