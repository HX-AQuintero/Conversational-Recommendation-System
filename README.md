## Conversational-Recommendation-System

### Summary

This project is a serverless conversational recommendation system built using AWS Bedrock and Anthropic Claude Sonnet v2. It simulates natural, human-like dialogue to deliver personalized recommendations for accommodation and restaurant services through AI Agent orchestration.

The system features a **Supervisor Agent** that interprets user intents and dynamically delegates tasks to specialized sub-agents depending on the service requested (e.g., hotel, Airbnb, fine dining). 

Users can interact naturally, with the system prompting for any missing context:
- For **accommodation**, it determines user preferences like hotel vs. Airbnb, and optional amenities such as pet-friendliness, sauna, or pool.
- For **restaurants**, it checks interest in fine dining to tailor results appropriately.

Real-time filtering and data retrieval is handled by AWS Lambda, querying information stored in S3 buckets. The system is designed to minimize assumptions, ensuring relevant and accurate recommendations by always requesting key missing information before responding.

Ideal for use in travel assistants, hospitality bots, and AI-powered recommendation platforms.

### 🔧 Tools & Technologies

**AWS Bedrock**: Hosts Claude models and manages orchestration of foundation models.

**Anthropic Claude Sonnet v2**: Powers natural language understanding and contextual agent interaction.

**AWS Lambda**: Provides serverless backend logic for handling requests and filtering data dynamically.

**AWS S3**: Stores data sets used for recommendation, and serves as the source for real-time queries.

**Python**: Implements agent orchestration logic, prompt management, and API integration.

### 💡 What it does

- Orchestrates multi-agent conversations using a Supervisor-Agent framework.

- Provides personalized accommodation recommendations (e.g., hotel vs. Airbnb, amenities).

- Offers restaurant suggestions based on dining preferences (e.g., fine dining or casual).

- Fetches and filters data from S3 in real time using serverless Lambda functions.

- Simulates context-aware, natural conversation flows by prompting for missing user input.
