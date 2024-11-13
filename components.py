from fasthtml.common import *
from dataclasses import dataclass
from lucide_fasthtml import Lucide


def TopBar():
    return Header(
        Div(
            Div(
                A(
                    H1(
                        "collins",
                        Span(".data", cls="text-red-500"),
                        cls="text-2xl font-bold text-darkblue-800 dark:text-gray-200",
                    ),
                    P(
                        "data scientist & analyst",
                        cls="text-sm text-darkblue-600 dark:text-gray-400",
                    ),
                    href="/",
                ),
            ),
            Nav(
                A(
                    "About",
                    href="/about",
                    cls="text-darkblue-800 dark:text-gray-200 hover:text-red-400 transition-colors",
                ),
                A(
                    "Projects",
                    href="/projects",
                    cls="text-darkblue-800 dark:text-gray-200 hover:text-red-400 transition-colors",
                ),
                A(
                    "Thoughts",
                    href="/thoughts",
                    cls="text-darkblue-800 dark:text-gray-200 hover:text-red-400 transition-colors",
                ),
                cls="flex space-x-4",
            ),
            Div(
                Button(
                    Div(
                        Div(
                            Lucide(
                                icon="moon", cls="text-darkblue-800 transition-colors"
                            ),
                            cls="absolute transform transition-all duration-300 dark:-rotate-90 dark:opacity-0",
                        ),
                        Div(
                            Lucide(icon="sun", cls="text-gray-200 transition-colors"),
                            cls="absolute transform transition-all duration-300 rotate-90 opacity-0 dark:rotate-0 dark:opacity-100",
                        ),
                        cls="flex w-5 h-5 items-center",
                    ),
                    cls="p-2 hover:bg-black hover:bg-opacity-10 dark:hover:bg-white dark:hover:bg-opacity-10 rounded-lg transition-colors",
                    onclick="toggleDarkMode()",
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
                        cls="text-red-500 text-2xl mr-3 transition-colors duration-300 group-hover:text-darkblue-800 dark:group-hover:text-gray-200",
                    ),
                    H3(
                        self.title,
                        cls="text-lg font-semibold transition-colors duration-300 group-hover:text-red-500 dark:group-hover:text-gray-200",
                    ),
                    cls="flex items-center mb-2",
                ),
                P(self.description, cls="text-sm text-gray-600 dark:text-gray-400"),
                href=self.endpoint,  # Use the endpoint for the link
                cls="block",
            ),
            cls="project-card bg-white dark:bg-slate-900 border border-gray-200 rounded-lg p-4 mb-4 transition-all duration-300 hover:border-red-500 hover:shadow-md group",
        )
