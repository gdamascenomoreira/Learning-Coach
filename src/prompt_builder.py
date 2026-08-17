SYSTEM_PROMPT = """
You are Learning Coach.

Help users:
- Create learning plans
- Identify skill gaps
- Recommend certifications
- Recommend projects
- Track progress
- Convert learning into career growth

Be practical and action-oriented.
"""


def build_prompt(profile, question):

    return f"""
User Profile

Current Role:
{profile["current_role"]}

Experience:
{profile["experience"]}

Career Goal:
{profile["career_goal"]}

Skills:
{", ".join(profile["skills"])}

Certifications:
{", ".join(profile["certifications"])}

Weekly Learning Hours:
{profile["weekly_learning_hours"]}

Question:
{question}

Provide:
1. Assessment
2. Recommendations
3. Next Steps
"""
