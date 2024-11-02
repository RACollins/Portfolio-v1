from fasthtml.common import *
from dataclasses import dataclass
from lucide_fasthtml import Lucide


def TopBar():
    return Header(
        Div(
            Div(
                H1(
                    "collins",
                    Span(".data", cls="text-red-500"),
                    cls="text-2xl font-bold text-darkblue-800",
                ),
                P("data scientist & analyst", cls="text-sm text-darkblue-800"),
            ),
            Nav(
                P(
                    "About",
                    href="#",
                    cls="text-darkblue-800 hover:text-red-400 transition-colors",
                ),
                P(
                    "Projects",
                    href="#",
                    cls="text-darkblue-800 hover:text-red-400 transition-colors",
                ),
                P(
                    "Publications",
                    href="#",
                    cls="text-darkblue-800 hover:text-red-400 transition-colors",
                ),
                cls="flex space-x-4",
            ),
            Div(
                Button(
                    Lucide(icon="moon"),
                    cls="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition-colors",
                    onclick="document.documentElement.classList.toggle('dark')",
                ),
                cls="flex justify-end p-4",
            ),
            Img(
                src="/assets/2020-07-06.jpg?height=40&width=40",
                alt="Profile",
                width="{40}",
                height="{40}",
                cls="rounded-full",
            ),
            cls="flex justify-between items-center max-w-3xl mx-auto px-4 w-full",
        ),
        cls="mb-6 pt-6",
    )


@dataclass
class ProjectCard:
    icon: str
    title: str
    description: str
    endpoint: str

    def __ft__(self):
        return Div(
            A(
                Div(
                    Div(
                        self.icon,
                        cls="text-red-500 text-2xl mr-3 transition-colors duration-300 group-hover:text-slate-500",
                    ),
                    H3(
                        self.title,
                        cls="text-lg font-semibold transition-colors duration-300 group-hover:text-red-500",
                    ),
                    cls="flex items-center mb-2",
                ),
                P(self.description, cls="text-sm text-gray-600"),
                href=self.endpoint,  # Use the endpoint for the link
                cls="block",
            ),
            cls="project-card bg-white border border-gray-200 rounded-lg p-4 mb-4 transition-all duration-300 hover:border-red-500 hover:shadow-md group",
        )
