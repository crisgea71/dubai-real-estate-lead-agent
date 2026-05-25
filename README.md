# Dubai Real Estate AI Lead Qualification Agent

An AI-powered lead qualification agent for real estate agencies in Dubai and the Middle East.

This agent helps qualify potential property clients before a human real estate agent calls them.

## What the agent does

The AI assistant asks the lead a series of qualification questions:

- Are they looking to buy or rent?
- What is their budget?
- Which area are they interested in?
- What property type are they looking for?
- When do they want to move or buy?
- Are they a cash buyer or do they need a mortgage?
- Do they want to schedule a viewing?
- What is their name and contact information?

At the end, the agent generates a structured lead summary.

## Lead Summary Output

The final summary includes:

- Client name
- Buy/Rent
- Budget
- Area
- Property type
- Timeline
- Mortgage/Cash
- Viewing interest
- Contact details
- Lead score: Hot / Warm / Cold
- Suggested next action for the real estate agent

## Use Case

This demo is designed for real estate agencies that want to save time by qualifying leads before a human agent follows up.

It can help agencies:

- reduce time spent on unqualified leads
- identify serious buyers or renters faster
- prepare structured lead information for agents
- improve response speed for website visitors

## Tech Stack

- Python
- Flask
- Groq API
- Llama 3.3 70B
- HTML
- CSS
- JavaScript
- Render deployment

## Local Setup

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
