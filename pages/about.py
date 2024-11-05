from fasthtml.common import *
from components import TopBar


def AboutPage():
    about_style = "max-w-3xl mx-auto px-4 mb-6 text-darkblue-800 dark:text-gray-300"
    return Div(
        TopBar(),
        Main(
            H2(
                "About",
                cls="max-w-3xl mx-auto px-4 mb-4 text-3xl font-bold text-darkblue-800 dark:text-gray-200",
            ),
            P(
                "With over eight years of experience as a data scientist, I specialize in developing sophisticated forecasting solutions using machine learning and artificial intelligence. My expertise lies in transforming complex data into actionable insights that drive business decisions and operational efficiency.",
                cls=about_style,
            ),
            P(
                "My journey has taken me through various sectors, from business intelligence and sales forecasting to my current focus on weather forecasting and risk mitigation in transport and logistics. I've developed and implemented predictive models that help organizations anticipate weather-related disruptions, optimize routing, and enhance operational resilience.",
                cls=about_style,
            ),
            P(
                "I'm passionate about leveraging data to solve real-world challenges, particularly in helping businesses navigate the complexities of weather-dependent operations. My approach combines rigorous statistical analysis with practical business acumen to deliver solutions that make a tangible impact.",
                cls=about_style,
            ),
            cls="py-8",
        ),
        cls="min-h-screen bg-[radial-gradient(ellipse_at_top_left,_#fff0d1_0%,_#ffffff_60%,_#cce6ff_100%)] dark:bg-[radial-gradient(ellipse_at_top_left,_#003196_0%,_#000000_60%,_#6a3400_100%)] animate-gradientX-top-left",
    )
