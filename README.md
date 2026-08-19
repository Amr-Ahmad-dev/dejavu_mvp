Déjà Vu — Smart Outing Recommendation Platform
<p align="center"> <strong>Helping students and young adults answer one simple question: “أروح فين؟” — Where do I go?</strong> </p> <p align="center"> Budget-first discovery · Group matching · Vibe-based recommendations · Hidden gems · Verified reviews </p> <p align="center"> <a href="mailto:amrahmadsalah@gmail.com">amrahmadsalah@gmail.com</a> &nbsp;•&nbsp; <a href="https://github.com/Amr-Ahmad-dev">GitHub</a> </p>
About

Déjà Vu is a smart outing recommendation platform built as an MVP around a real user problem identified through the DÉJÀ VU × INNOVEGYPT research and ideation process.

The problem was simple:

“أروح فين؟” — Where do I go?

Students and young adults can spend a significant amount of time deciding where to go, especially when planning with friends. Budget constraints, uncertainty about places, unreliable reviews, and different preferences within a group can make a simple outing surprisingly difficult to plan.

Déjà Vu approaches the problem from the user's constraints rather than starting with a generic list of places.

Instead of asking:

“What kind of place are you looking for?”

the application can start with:

“How much do you want to spend, what kind of experience do you want, and who are you going with?”

What I Built

The MVP focuses on the highest-scoring ideas from the original ideation exercise.

Feature	Purpose
💰 Reverse Budget-First Search	Find places based on maximum spending per person
👥 Group Swipe-to-Match	Let multiple people independently choose places and find common matches
🎭 Vibe & Mood Filtering	Discover places by experience rather than only category
💎 Hidden Gem Discovery	Give lesser-known places additional visibility
⭐ Verified-Visit Reviews	Distinguish reviews marked as coming from an actual visit
🧮 Group Cost Estimation	Estimate the expected cost based on group size

The Group Swipe-to-Match feature received the highest score during the ideation process and became one of the central interaction patterns of the MVP.

How It Works
1. Start With Your Budget

Instead of browsing hundreds of places and checking prices individually, the user specifies a maximum amount they are willing to spend per person.

Maximum budget
      ↓
Filter available places
      ↓
Show affordable options

The discover page also estimates the expected cost for the selected group size.

2. Choose the Experience

Users can filter places using vibe-oriented tags such as:

Chill
Study-Friendly
Romantic
Social
Outdoor
And other experience-oriented tags

This allows the recommendation process to represent what the user wants to feel or do, rather than relying entirely on traditional categories such as restaurants or cafés.

3. Discover Places

The platform combines:

Budget
Category
Vibe
Group size
Hidden-gem status

to narrow the available options.

Hidden-gem locations receive additional visibility so that discovery does not become limited to the most obvious or popular places.

4. Match With Friends

A group can create a shared room and distribute a room code.

Each participant can independently swipe through places.

             Group Room
                 │
       ┌─────────┼─────────┐
       ↓         ↓         ↓
    Person A  Person B  Person C
       │         │         │
       └─────────┼─────────┘
                 ↓
          Shared preferences
                 ↓
           Common matches

A place becomes a match when the current members of the room have all liked it.

This turns the problem from:

“Where should we go?”

into:

“Which places do we all agree on?”

Research → Product

Déjà Vu was not designed by randomly selecting features.

The MVP was built from the DÉJÀ VU × INNOVEGYPT research process, including:

Problem identification
Empathy maps
Persona development
Point of View (POV)
Business Model Canvas
Ideation
Idea scoring
Feature clustering

The highest-value ideas were then translated into concrete product functionality.

Ideation Results
Idea	Score	Implementation
Reverse Budget-First Search	7/9	Implemented
Group Swipe-to-Match	8/9	Implemented
Vibe & Mood Filtering	7/9	Implemented
Verified-Visit Reviews	—	MVP implementation
Hidden Gem Discovery	—	Implemented

This created a direct connection between user research → prioritization → product design → implementation.

Core Features
💰 Budget-First Discovery

Users can define a maximum spending amount per person and receive places that fit within that constraint.

The system also calculates an estimated total based on the selected group size.

Price per person × Group size
                ↓
        Estimated outing cost

This reduces the need to manually calculate whether a place fits the group's budget.

👥 Group Swipe-to-Match

Groups can create a shared room using a room code.

Each member makes independent decisions about places.

The system stores each member's swipe and checks for common preferences.

Matching logic

A simplified representation is:

Likes(A) ∩ Likes(B) ∩ Likes(C) ...
                    ↓
             Common places
                    ↓
                 Matches

The room can therefore identify places that satisfy the preferences of the entire group rather than only one person.

🎭 Vibe & Mood Discovery

Traditional place discovery often depends heavily on categories.

Déjà Vu adds another layer:

What kind of experience are you looking for?

The MVP includes eight vibe-oriented tags, allowing places to be discovered through characteristics such as:

Chill
Study-Friendly
Romantic
Social
Outdoor

This makes the filtering model closer to the way people actually describe an outing.

💎 Hidden Gems

The application includes a mechanism for identifying places as hidden gems.

These places receive additional visibility on the homepage and priority within discovery results.

The purpose is to prevent recommendation systems from repeatedly surfacing only the most obvious locations.

⭐ Verified-Visit Reviews

Reviews include a verified_visit state.

For the MVP, verification is represented by a confirmation mechanism rather than actual location or purchase verification.

MVP
User confirmation
      ↓
verified_visit = true

A future implementation could replace this with stronger evidence such as:

GPS verification
Receipt verification
Booking verification

The current approach intentionally keeps the MVP simple enough to test the underlying product idea before implementing a more complicated verification system.

Data Model

The application uses a relational SQLite database.

Main entities
place
 ├── name
 ├── category
 ├── area
 ├── price/person
 ├── hidden-gem flag
 └── verified flag


category
 └── lookup data


vibe
 └── lookup data


place_vibe
 └── place ↔ vibe relationship


review
 ├── rating
 ├── comment
 └── verified_visit


room
 └── group matching session


room_member
 └── users participating in a room


room_swipe
 └── individual group decisions

The many-to-many relationship between places and vibes is represented through place_vibe.

Application Structure
app.py
│
├── Routes
├── Application logic
└── Database queries


schema.sql
│
└── SQLite database structure


seed.py
│
└── Demo data generation


templates/
│
└── Jinja2 pages


static/
├── css/
│   └── style.css
│
└── js/
    ├── swipe.js
    └── main.js
Main files

app.py

Contains the application's routes, request handling, and database interactions.

schema.sql

Defines the SQLite database schema and relationships.

seed.py

Creates the database and populates it with demo data representing 25 Cairo places across five categories.

templates/

Contains the Jinja2 templates used to render the application.

static/css/style.css

Contains the application's visual design system, including the Cairo Dusk visual theme.

static/js/swipe.js

Handles the swipe-card interaction, including drag and tap behavior and match polling.

static/js/main.js

Handles smaller client-side interactions such as dismissing flash messages.

Technology Stack
Backend
Python
Flask
SQLite
Frontend
HTML
CSS
JavaScript
Jinja2
Development Concepts
MVC-style application structure
Relational database design
SQL queries
Many-to-many relationships
Session-based group rooms
Client-side interaction
Asynchronous match polling
Form handling
Server-side rendering
Filtering and search
Recommendation logic
Product-oriented MVP development
Running the Project
Requirements
Python 3
pip
Installation

Clone the repository and install the dependencies:

pip install -r requirements.txt
Initialize the Database

Run:

python seed.py

This creates:

dejavu.db

and populates it with demo data.

Start the Application
python app.py

Then open:

http://localhost:5000
Example User Journey

A typical outing-planning flow looks like this:

Home
  ↓
Set budget
  ↓
Choose vibe / filters
  ↓
Discover places
  ↓
Create group room
  ↓
Share room code
  ↓
Everyone swipes
  ↓
Common preferences identified
  ↓
Matching places displayed
  ↓
Choose where to go

The entire flow is designed around reducing decision friction rather than simply providing another directory of places.

MVP Scope

The project intentionally focuses on validating the core recommendation and group-decision experience.

Implemented
Budget-first search
Group swipe matching
Room codes
Vibe filtering
Hidden-gem discovery
Reviews
Verified-visit state
Group cost estimation
Cairo demo dataset
Responsive interactive UI
Intentionally Deferred

The following were kept outside the MVP:

Real user authentication
Real GPS-based visit verification
Receipt-based verification
Payments
Booking commissions
Merchant/business dashboard
Live chatbot assistant

These features can be introduced after validating the core product with real users.

Future Development

Possible next steps include:

Real user accounts and authentication
GPS-based visit verification
Receipt or booking verification
Live place data
Real-time availability
Booking integration
Merchant dashboard
Personalized recommendations
Improved recommendation ranking
Chatbot-based natural-language discovery
Analytics based on real user behavior
Production deployment
Product Design Philosophy

The main design decision behind Déjà Vu is simple:

Start with the user's constraints, not the database's categories.

A traditional discovery experience might begin with:

Restaurant
Café
Park
Entertainment
Shopping

Déjà Vu adds another layer:

How much can I spend?
Who am I going with?
What kind of experience do I want?
What places might we all enjoy?

The result is a recommendation experience designed around decision-making, rather than simply browsing.

Current Status

MVP — Functional prototype

Déjà Vu is currently an MVP designed to test the core product concept and interaction model.

Some production-level systems have intentionally been simplified or simulated so that the central recommendation and group-matching experience can be developed and evaluated first.

The project is therefore best understood as a functional product prototype, not a production-ready commercial platform.

What This Project Demonstrates

This project combines software development with product discovery and user-centered design.

It demonstrates experience with:

Translating user research into software requirements
Prioritizing features using ideation scores
Designing an MVP around a specific problem
Building a Flask web application
Designing a relational SQLite database
Implementing filtering and recommendation logic
Building interactive JavaScript components
Designing group decision-making workflows
Implementing many-to-many relationships
Building server-rendered interfaces with Jinja2
Designing a consistent visual system
Separating MVP functionality from future production requirements

The project was particularly useful for understanding that building the software is only one part of product development.

The harder question is deciding what should actually be built first and why.

Contact
<p align="center"> <strong>Amr Ahmad</strong><br> Computer Science Student </p> <p align="center"> <a href="mailto:amrahmadsalah@gmail.com">amrahmadsalah@gmail.com</a> &nbsp;•&nbsp; <a href="https://github.com/Amr-Ahmad-dev">GitHub</a> </p>
<p align="center"> <strong>Déjà Vu</strong><br> Smart outing discovery for better decisions, better groups, and better places. </p> <p align="center"> Python · Flask · SQLite · Jinja2 · JavaScript · Product Design · User Research </p>
