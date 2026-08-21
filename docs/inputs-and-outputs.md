# Inputs and Outputs

## Purpose

Learning Coach helps users transform learning activities into actionable career growth plans through personalized recommendations.

---

# Inputs

The Learning Coach uses the following information provided by the user:

## User Profile

- Name
- Current Role
- Years of Experience
- Career Goal
- Interests

## Learning Data

- Completed Learning Activities
- Certifications Earned
- Courses Completed
- Books Read
- Projects Completed

## Goals

- Learning Goals
- Career Milestones
- Target Certifications
- Desired Job Role

## User Requests

Examples:

- What should I learn next?
- Which certification should I pursue?
- Recommend a project for my career goal.
- Create a learning plan.

---

# Outputs

The Learning Coach generates personalized recommendations based on the user's profile and goals.

## Learning Recommendations

- Suggested courses
- Suggested books
- Suggested learning paths
- Suggested certifications

## Career Recommendations

- Career guidance
- Skill gap analysis
- Next career steps
- Recommended focus areas

## Project Recommendations

- Beginner projects
- Intermediate projects
- Advanced projects
- Portfolio ideas

## Personalized Plans

- Learning plans
- Certification roadmaps
- Career development plans

## Progress Insights

- Learning progress summary
- Completed milestones
- Remaining goals
- Recommended next actions

---

# Example

## Input

Current Role: Azure Support Engineer

Career Goal: Azure AI Engineer

Interests:

- Artificial Intelligence
- Cloud Architecture

Completed Certifications:

- AZ-104
- AZ-305

## Output

Learning Plan:

- Complete AI-103 Learning Path
- Build a Retrieval-Augmented Generation (RAG) project
- Earn Azure AI Engineer certification

Recommended Project:

- Learning Coach agent using Azure AI Foundry

Recommended Next Step:

- Implement tool calling and Azure AI
  
  
# User Profile Schema

The Learning Coach stores user information in a profile object.

Example:

{
  "name": "",
  "current_role": "",
  "experience": "",
  "career_goal": "",
  "weekly_learning_hours": 0,
  "certifications": [],
  "skills": [],
  "interests": [],
  "projects": [],
  "books": [],
  "courses": [],
  "completed_learning_activities": [],
  "learning_goals": [],
  "career_milestones": []
}