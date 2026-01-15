# Casa Amigo 🏠 (Portfolio Case Study)

This repository documents my individual contributions to *Casa Amigo*, a team-built AI chatbot designed to support property inquiries and tenant services in the real estate domain.

## Project Overview

Casa Amigo is an AI-powered rental assistant that supports tenants and property managers by:
- Answering tenancy-related questions using retrieval-augmented generation (RAG)
- Providing neighborhood and property insights
- Managing tenant reminders and rental milestones

This project was developed collaboratively as a team.  
This repository focuses **only on my individual contributions**.

## My Contributions

### 1. UI / UX Design
- Collaborated on user-facing layouts and interaction flows for the chatbot interface and dashboards.
- Designed custom logos and logo animations for the application branding.
- Implemented custom sidebar cursor styling to enhance user experience.
- Contributed to usability improvements for tenant-facing workflows in the Streamlit-based frontend.

### 2. Property Listing Data Ingestion
- Built a web-scraping pipeline to collect public property listings from PropertyGuru.
- Cleaned and structured listing data before uploading to Supabase (PostgreSQL).
- Enabled the team to work with realistic property datasets during development.

### 3. Tenant Agreement Parser & Supabase Uploader *(Prototype)*
- Implemented a parser to extract structured information from tenant agreement documents.
- Built a Supabase uploader to store parsed clauses and metadata.
- This feature was not integrated into the final product due to time constraints, but demonstrates extensibility for future contract ingestion.

### 4. Database Seeding
- Created and populated sample user datasets in Supabase to support development, testing, and demos.

### 5. Evaluation Question Design
- Designed evaluation question sets to assess ROUGE metrics and retrieval quality of the RAG system.
- Focused on common tenant inquiries and contract-related edge cases to benchmark system performance.

## Selected Design & Data Flows

The following illustrate the components I designed or implemented.

## Technologies Used (My Scope)

- Python
- Supabase (PostgreSQL)
- Web scraping tools (BeautifulSoup / Requests)
- Streamlit (UI prototyping)
- Document parsing (PDF/text processing)

## Team Acknowledgement

Casa Amigo was developed as a team project.  
The full system architecture, agentic workflows, backend services, and deployment were implemented collaboratively.

🔗 Original team repository: https://github.com/s-hreya-riram/casa-amigo
