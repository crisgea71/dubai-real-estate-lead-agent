# LeadQual AI – AI Lead Qualification Agent for Dubai Real Estate

LeadQual AI helps real estate agencies qualify website visitors before a human agent spends time calling them.

It starts a natural conversation with potential buyers or renters, collects the key qualification details, scores the lead, and generates a structured summary that a real estate agent can use for follow-up.

## Live Demo
Live demo: [Try LeadQual AI](https://dubai-real-estate-lead-agent.onrender.com)

## Who This Is For

This demo is designed for:

- Real estate agencies in Dubai and the Middle East
- Brokers who receive website inquiries
- Agencies that want to filter low-quality leads before calling
- Teams that want faster handoff from website chat to human agent
- Businesses planning to connect AI qualification with WhatsApp, Google Sheets, or CRM systems

## The Problem

Real estate agents often spend time calling leads who are not ready, do not have a clear budget, or are just browsing.

LeadQual AI helps solve this by asking the first qualification questions automatically before the human agent gets involved.

## What the Agent Does

The AI assistant asks each website visitor:

- Are they looking to buy or rent?
- What is their budget?
- Which area are they interested in?
- What property type are they looking for?
- When do they want to move or buy?
- Are they a cash buyer or do they need a mortgage?
- Do they want to schedule a viewing?
- What is their name and contact information?

At the end of the conversation, the agent generates a structured lead summary.

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

## Lead Scoring Logic

| Hot Lead | Warm Lead | Cold Lead |
|---|---|---|
| Clear budget | Some clear preferences | Just browsing |
| Clear area | Budget or area is partly clear | Unsure about budget |
| Short timeline | Medium-term timeline | Unsure about area |
| Strong buying/renting intent | Interested but not urgent | No clear timeline |
| Wants a viewing | May need follow-up later | Not ready to move or buy soon |
| Cash buyer or mortgage plan | Needs more nurturing | Low immediate intent |

## Key Benefits

- Reduces repetitive lead qualification work
- Helps agents focus on more serious prospects
- Creates a consistent first response for every website visitor
- Generates structured lead data for follow-up
- Helps separate hot leads from casual inquiries
- Can be extended with WhatsApp Business API, CRM, or Google Sheets

## Suggested Real-World Workflow

For a real estate agency, the production workflow could look like this:

```text
Website visitor
↓
AI lead qualification conversation
↓
Structured lead summary
↓
WhatsApp Business API alert to human agent
↓
Optional Google Sheets / CRM storage
↓
Human agent follow-up
```

## Current Demo Features

- Website-based AI chat interface
- Real estate lead qualification flow
- Groq API integration with Llama 3.3 70B
- Structured lead summary generation
- Hot / Warm / Cold lead scoring
- Suggested next action for the human agent
- Demo access limit
- Password unlock for controlled access
- Render deployment support

## Future Improvements

This is the first demo version of the AI lead qualification agent.

Possible next upgrades:

- Add Arabic language support for Dubai and Middle East users
- Send the lead summary to a human real estate agent via WhatsApp Business API
- Save qualified leads into Google Sheets
- Connect the agent to a CRM such as HubSpot, Zoho, Pipedrive, or Salesforce
- Connect to live property listings or an internal property database
- Add booking flow for property viewings
- Add a dashboard where agents and managers can see all leads
- Assign leads automatically to different agents
- Add follow-up reminders for warm and cold leads
- Add lead analytics and conversion tracking

## For Developers

### Tech Stack

- Python
- Flask
- Groq API
- Llama 3.3 70B
- HTML
- CSS
- JavaScript
- Render

## Local Setup

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```bash
GROQ_API_KEY=your_groq_api_key_here
DEMO_PASSWORD=your_demo_password_here
FLASK_SECRET_KEY=your_flask_secret_key_here
```

Run the app locally:

```bash
python3 app.py
```

Open in browser:

```bash
http://127.0.0.1:5001
```

## Environment Variables

This project uses environment variables for sensitive information.

Required variables:

- `GROQ_API_KEY`
- `DEMO_PASSWORD`
- `FLASK_SECRET_KEY`

The real `.env` file is ignored by Git and should never be uploaded to GitHub.

## Render Deployment

The app is prepared for deployment on Render.

Recommended Render settings:

```bash
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

Required Render environment variables:

```bash
GROQ_API_KEY=your_real_groq_api_key
DEMO_PASSWORD=your_demo_password
FLASK_SECRET_KEY=your_flask_secret_key
```

## Demo Access

The demo includes limited access and password unlock functionality.

This allows the project to be shown publicly while keeping full access controlled.

The demo password should not be stored inside the public README or hardcoded in the repository. It should be stored as an environment variable.

## Status

**v1.0 – Live MVP Demo**

Current version includes:

- Live website demo
- AI-powered real estate lead qualification
- Groq API connection
- Lead summary generation
- Hot / Warm / Cold lead scoring
- Demo limit and password unlock
- Future WhatsApp Business API and CRM integrations planned
