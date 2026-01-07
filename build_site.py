import os
import random

# 1. SETUP: Create a folder for your output
output_folder = "site_pages"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 2. THE DATA: Your High-Paying Affiliate Tools
# In a real build, these links would be your specific affiliate tracking URLs.
tools = [
    {
        "name": "Notion AI",
        "category": "Organization",
        "benefit": "organize client notes and contracts",
        "link": "https://affiliate.notion.so/YOUR_ID",
        "price": "$10/mo"
    },
    {
        "name": "Jasper",
        "category": "Marketing",
        "benefit": "write emails and marketing copy in seconds",
        "link": "https://jasper.ai?fpr=YOUR_ID",
        "price": "$39/mo"
    },
    {
        "name": "Synthesia",
        "category": "Video",
        "benefit": "create professional training videos without a camera",
        "link": "https://synthesia.io/?via=YOUR_ID",
        "price": "$29/mo"
    },
    {
        "name": "FreshBooks", 
        "category": "Finance",
        "benefit": "automate invoicing and expense tracking",
        "link": "https://freshbooks.com/partner/YOUR_ID", # Example non-AI tool that fits
        "price": "$15/mo"
    }
]

# 3. THE TARGETS: Professions that need help (but are ignored by big blogs)
# We map specific "pain points" to each profession to make the content unique.
professions = [
    {"title": "Plumbers", "slug": "plumbers", "pain": "scheduling jobs and invoicing clients"},
    {"title": "Real Estate Agents", "slug": "real-estate-agents", "pain": "writing listing descriptions and managing leads"},
    {"title": "Wedding Planners", "slug": "wedding-planners", "pain": "coordinating vendors and managing timelines"},
    {"title": "Personal Trainers", "slug": "personal-trainers", "pain": "creating workout plans and tracking client progress"},
    {"title": "Pastors", "slug": "pastors", "pain": "researching sermons and organizing community events"},
    {"title": "Dentists", "slug": "dentists", "pain": "managing patient appointments and reminders"},
    {"title": "Freelance Writers", "slug": "freelance-writers", "pain": "beating writer's block and editing drafts"},
]

# 4. THE ENGINE: The HTML Template
# We use f-strings to inject data dynamically.
def generate_html(profession, tool_list):
    # Select 3 random tools to feature so every page isn't identical
    featured_tools = random.sample(tool_list, 3)
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Best AI Tools for {profession['title']} in 2025</title>
        <meta name="description" content="Discover the top rated AI software for {profession['title']} to help with {profession['pain']}. Automation guides for {profession['title']}.">
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
            header {{ background: #f4f4f4; padding: 40px 20px; text-align: center; border-radius: 8px; margin-bottom: 40px; }}
            h1 {{ margin: 0; color: #2c3e50; }}
            .tool-card {{ border: 1px solid #e1e1e1; padding: 20px; border-radius: 8px; margin-bottom: 20px; transition: transform 0.2s; }}
            .tool-card:hover {{ transform: translateY(-3px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }}
            .btn {{ display: inline-block; background: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 4px; font-weight: bold; margin-top: 10px; }}
            .tag {{ background: #e1f0ff; color: #007bff; padding: 4px 8px; border-radius: 4px; font-size: 0.8em; text-transform: uppercase; letter-spacing: 1px; }}
        </style>
    </head>
    <body>
        <header>
            <h1>The 3 Best AI Tools for {profession['title']}</h1>
            <p>Stop wasting time on {profession['pain']}. Here is the software stack used by top {profession['title']} in 2025.</p>
        </header>

        <section>
            <h2>Why {profession['title']} Need AI Today</h2>
            <p>The landscape for {profession['title']} is changing. Clients expect faster responses and better organization. 
            The tools below were selected specifically because they help {profession['title']} {profession['pain']} more efficiently.</p>
        </section>

        <section>
            <h2>Top Recommended Software</h2>
            {''.join([f'''
            <div class="tool-card">
                <span class="tag">{tool['category']}</span>
                <h3>{tool['name']}</h3>
                <p><strong>Best for:</strong> Helping {profession['title'].lower()} {tool['benefit']}.</p>
                <p>Price: {tool['price']}</p>
                <a href="{tool['link']}" class="btn" target="_blank" rel="nofollow">Try {tool['name']} Free</a>
            </div>
            ''' for tool in featured_tools])}
        </section>

        <footer>
            <p>&copy; 2025 TaskFlow AI Directory. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """
    return html_content

# 5. EXECUTION: Generate the files
print(f"Starting generation for {len(professions)} professions...")

for prof in professions:
    filename = f"ai-for-{prof['slug']}.html"
    filepath = os.path.join(output_folder, filename)
    
    content = generate_html(prof, tools)
    
    with open(filepath, "w") as f:
        f.write(content)
    
    print(f"Generated: {filename}")

print("\nDone! Open the 'site_pages' folder to see your website.")