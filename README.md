cat > README.md << 'EOF'
# Dubai Real Estate AI Lead Qualification Agent

An AI-powered lead qualification agent for real estate agencies in Dubai and the Middle East.

The agent helps qualify potential property clients before a human real estate agent calls them.

## What it does

The AI agent asks the lead:

- Buy or rent
- Budget
- Preferred area
- Property type
- Timeline
- Cash or mortgage
- Viewing interest
- Name and contact details

At the end, it generates a structured lead summary:

- Client name
- Buy/Rent
- Budget
- Area
- Property type
- Timeline
- Mortgage/Cash
- Viewing
- Contact
- Lead score: Hot / Warm / Cold
- Suggested next action

## Tech Stack

- Python
- Flask
- Groq API
- Llama 3.3 70B
- HTML/CSS/JavaScript
- Render-ready deployment

## Local Setup

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
