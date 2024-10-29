'use client'

import { useState } from 'react'
import Image from 'next/image'
import Link from 'next/link'
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { BarChart, PieChart, Database, Code, MessageSquare, Send, Network, X } from 'lucide-react'

export default function Home() {
  const [isChatOpen, setIsChatOpen] = useState(false)

  return (
    <div className="min-h-screen bg-gradient-to-br from-[#F2E8CF] via-white to-[#4A7296]/10">
      <div className="max-w-3xl mx-auto px-4 py-8">
        <header className="flex justify-between items-center mb-12">
          <div>
            <h1 className="text-2xl font-bold text-[#1A2E40]">kyoto<span className="text-[#D90429]">.data</span></h1>
            <p className="text-sm text-[#4A7296]">data scientist & analyst</p>
          </div>
          <nav className="flex space-x-4">
            <Link href="#" className="text-[#4A7296] hover:text-[#1A2E40] transition-colors">Projects</Link>
            <Link href="#" className="text-[#4A7296] hover:text-[#1A2E40] transition-colors">Publications</Link>
            <Link href="#" className="text-[#4A7296] hover:text-[#1A2E40] transition-colors">About</Link>
          </nav>
          <Image
            src="/placeholder.svg?height=40&width=40"
            alt="Profile"
            width={40}
            height={40}
            className="rounded-full bg-[#5E0B15]"
          />
        </header>

        <main>
          <section className="mb-16 relative">
            <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2MCIgaGVpZ2h0PSI2MCI+CiAgPHBhdGggZD0iTTAgMGg2MHY2MEgweiIgZmlsbD0ibm9uZSIgLz4KICA8cGF0aCBkPSJNMzAgMzBtLTI4IDAgYTI4IDI4IDAgMSAwIDU2IDAgYTI4IDI4IDAgMSAwIC01NiAwIiBmaWxsPSJub25lIiBzdHJva2U9IiM0QTcyOTYiIHN0cm9rZS13aWR0aD0iMC41IiBvcGFjaXR5PSIwLjEiIC8+CiAgPHBhdGggZD0iTTMwIDMwbTIwIDAgYTIwIDIwIDAgMSAxIC00MCAwIGEyMCAyMCAwIDEgMSA0MCAwIiBmaWxsPSJub25lIiBzdHJva2U9IiM0QTcyOTYiIHN0cm9rZS13aWR0aD0iMC41IiBvcGFjaXR5PSIwLjEiIC8+CiAgPHBhdGggZD0iTTMwIDMwbTEyIDAgYTEyIDEyIDAgMSAxIC0yNCAwIGExMiAxMiAwIDEgMSAyNCAwIiBmaWxsPSJub25lIiBzdHJva2U9IiM0QTcyOTYiIHN0cm9rZS13aWR0aD0iMC41IiBvcGFjaXR5PSIwLjEiIC8+Cjwvc3ZnPg==')] opacity-10" />
            <div className="relative">
              <h2 className="text-3xl font-bold mb-4 text-[#1A2E40]">Hi, I'm Kyoto — a data scientist and analyst.</h2>
              <p className="text-[#4A7296] mb-6">
                I transform complex data into actionable insights. With expertise in machine learning, statistical analysis, and data visualization, I help organizations make data-driven decisions.
              </p>
              <div className="flex flex-wrap gap-4 mb-6">
                <div className="flex items-center gap-2 text-[#D90429]">
                  <BarChart size={24} />
                  <span>Data Analysis</span>
                </div>
                <div className="flex items-center gap-2 text-[#5E0B15]">
                  <PieChart size={24} />
                  <span>Visualization</span>
                </div>
                <div className="flex items-center gap-2 text-[#1A2E40]">
                  <Code size={24} />
                  <span>Machine Learning</span>
                </div>
              </div>
            </div>
          </section>

          <section className="mb-16">
            <h3 className="text-xl font-semibold mb-6 text-[#1A2E40]">Featured Projects</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {[
                { title: "Predictive Analytics Dashboard", description: "Real-time prediction model for customer churn using machine learning algorithms.", icon: BarChart },
                { title: "NLP Sentiment Analysis Tool", description: "Sentiment analysis for social media data using advanced NLP techniques.", icon: Database },
                { title: "Time Series Forecasting", description: "Accurate sales forecasting model using ARIMA and Prophet.", icon: PieChart },
                { title: "Network Anomaly Detection", description: "AI-powered system for detecting anomalies in network traffic patterns.", icon: Network }
              ].map((project, index) => (
                <div key={index} className="border border-[#F2E8CF] p-6 rounded-lg transition-all duration-300 hover:shadow-lg hover:border-[#D90429] group bg-white bg-opacity-50 backdrop-blur-sm">
                  <div className="flex items-center gap-3 mb-3">
                    <project.icon className="text-[#D90429] group-hover:text-[#5E0B15] transition-colors" size={24} />
                    <h4 className="font-semibold text-[#1A2E40] group-hover:text-[#D90429] transition-colors">{project.title}</h4>
                  </div>
                  <p className="text-sm text-[#4A7296] group-hover:text-[#1A2E40] transition-colors">{project.description}</p>
                </div>
              ))}
            </div>
          </section>

          <section>
            <h3 className="text-xl font-semibold mb-6 text-[#1A2E40]">Recent Publications</h3>
            <ul className="space-y-4">
              {[
                { title: "Advancements in Unsupervised Learning Techniques", date: "15 Mar 2024" },
                { title: "Ethical Considerations in AI-Driven Decision Making", date: "02 Feb 2024" },
                { title: "Optimizing Neural Networks for Edge Computing", date: "18 Jan 2024" }
              ].map((publication, index) => (
                <li key={index} className="flex justify-between items-center">
                  <Link href="#" className="text-[#4A7296] hover:text-[#D90429] transition-colors">{publication.title}</Link>
                  <span className="text-sm text-[#1A2E40]">{publication.date}</span>
                </li>
              ))}
            </ul>
            <Button variant="link" className="mt-6 p-0 text-[#D90429] hover:text-[#5E0B15] transition-colors">View all publications →</Button>
          </section>
        </main>
      </div>

      <div className={`fixed z-50 transition-all duration-300 ${isChatOpen ? 'bottom-[320px] right-4' : 'bottom-4 right-4'}`}>
        <Button
          onClick={() => setIsChatOpen(!isChatOpen)}
          className="rounded-full w-12 h-12 bg-[#D90429] hover:bg-[#5E0B15] transition-colors shadow-lg"
          aria-label={isChatOpen ? "Close chat" : "Open chat"}
        >
          {isChatOpen ? <X className="text-white" /> : <MessageSquare className="text-white" />}
        </Button>
      </div>

      <Card className={`fixed bottom-4 right-4 w-80 bg-white rounded-lg shadow-lg transition-all duration-300 ease-in-out ${
        isChatOpen ? 'translate-y-0 opacity-100' : 'translate-y-full opacity-0 pointer-events-none'
      }`}>
        <CardContent className="p-4">
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-lg font-semibold text-[#1A2E40]">Chat with Kyoto</h3>
            <Button
              variant="ghost"
              size="icon"
              onClick={() => setIsChatOpen(false)}
              className="text-[#4A7296] hover:text-[#D90429]"
            >
              <X size={20} />
            </Button>
          </div>
          <div className="mb-4 h-40 overflow-y-auto bg-[#F2E8CF] p-2 rounded border border-[#4A7296]">
            {/* Chat messages would go here */}
            <p className="text-[#4A7296]">Hello! How can I assist you with data science today?</p>
          </div>
          <form className="flex gap-2">
            <Input
              type="text"
              placeholder="Type your message..."
              className="flex-grow border-[#4A7296] focus:ring-[#D90429]"
            />
            <Button type="submit" size="icon" className="bg-[#D90429] hover:bg-[#5E0B15]">
              <Send className="h-4 w-4" />
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  )
}