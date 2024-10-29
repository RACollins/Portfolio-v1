from fasthtml.common import *
from components import ProjectCard
from lucide_fasthtml import Lucide


def TopBar():
    return Header(
        Div(
            H1(
                "collins",
                Span(".data", cls="text-primary"),
                cls="text-2xl font-bold text-text_primary",
            ),
            P("data scientist & analyst", cls="text-sm text-text_primary"),
        ),
        Nav(
            P(
                "Projects",
                href="#",
                cls="text-text_primary hover:text-primary transition-colors",
            ),
            P(
                "Publications",
                href="#",
                cls="text-text_primary hover:text-primary transition-colors",
            ),
            P(
                "About",
                href="#",
                cls="text-text_primary hover:text-primary transition-colors",
            ),
            cls="flex space-x-4",
        ),
        Img(
            src="/assets/2020-07-06.jpg?height=40&width=40",
            alt="Profile",
            width="{40}",
            height="{40}",
            cls="rounded-full",
        ),
        cls="flex justify-between items-center mb-12",
    )


def SubHeader():
    return Section(
        Div(
            H2(
                "Hi, I'm Richard Collins — a data scientist and analyst.",
                cls="text-3xl font-bold mb-4 text-text_primary",
            ),
            P(
                "I transform complex data into actionable insights. With expertise in machine learning, statistical analysis, and data visualization, I help organisations make data-driven decisions.",
                cls="text-text_primary mb-6",
            ),
            Div(
                Div(
                    Lucide(icon="file-text"),
                    Span("CV"),
                    cls="flex items-center gap-2 text-text_primary hover:text-primary transition-colors",
                ),
                Div(
                    Lucide(icon="github"),
                    Span("GitHub"),
                    cls="flex items-center gap-2 text-text_primary hover:text-primary transition-colors",
                ),
                Div(
                    Lucide(icon="linkedin"),
                    Span("LinkedIn"),
                    cls="flex items-center gap-2 text-text_primary hover:text-primary transition-colors",
                ),
                cls="flex flex-wrap gap-4 mb-6",
            ),
            cls="relative",
        ),
        cls="mb-16 relative",
    )


def FeaturedProjects():
    return Section(
        H2("Featured Projects", cls="text-xl font-semibold mb-6 text-text_primary"),
        Div(
            Div(
                ProjectCard(Lucide(icon="audio-waveform"), "Project 1", "This is a description of Project 1", "/projects/1"),
                ProjectCard(Lucide(icon="chart-column-increasing"), "Project 2", "This is a description of Project 2", "/projects/2"),
                cls="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-4 text-text_primary"
            ),
            Div(
                ProjectCard(Lucide(icon="chart-network"), "Project 3", "This is a description of Project 3", "/projects/3"),
                ProjectCard(Lucide(icon="cloud-snow"), "Project 4", "This is a description of Project 4", "/projects/4"),
                cls="grid grid-cols-1 sm:grid-cols-2 gap-4 text-text_primary"
            ),
            cls="max-w-4xl mx-auto"
        ),
        cls="mb-16"
    )


def Page():
    return Div(
        Div(
            TopBar(),
            Main(SubHeader(), FeaturedProjects()),
            cls="max-w-3xl mx-auto px-4 py-8",
        ),
        cls="min-h-screen bg-gradient-to-br from-orange-100 via-transparent to-gray-100",
    )
