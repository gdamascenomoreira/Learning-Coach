def build_prompt(profile, question):

    prompt = f"""
You are Learning Coach.

User Profile

Current Role:
{profile['current_role']}

Experience:
{profile['experience']}

Career Goal:
{profile['career_goal']}

Skills:
{', '.join(profile['skills'])}

Certifications:
{', '.join(profile['certifications'])}

Weekly Learning Hours:
{profile['weekly_learning_hours']}

User Question:
{question}

Provide:

1. Analysis
2. Recommendations
3. Next Steps
"""

    return prompt
