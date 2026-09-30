# ===== Career Interest Recommender =====
print("===== Career Interest Recommender =====")
print()
print("Answer the following questions with: 1 (Yes) or 0 (No)")
print()
# Scores for each career path
scores = {
    "AI & Machine Learning": 0,
    "Web Development": 0,
    "Cybersecurity": 0,
    "Data Science": 0,
    "UI/UX Design": 0,
    "Cloud & Devops": 0}
# info: What Should You Study + Future options
study_plan = {
    "AI & Machine Learning": {
        "study": [
            "Python basics and libraries like NumPy, Pandas",
            "Math: linear algebra, probability, statistics",
            "Intro to machine learning concepts"],
        "Future Occupation": [
            "Machine Learning Engineer",
            "Data Scientist",
            "AI Engineer"]
    },
    "Web Development": {
        "study": [
            "HTML, CSS, basic JavaScript",
            "Python with Flask or Django",
            "Responsive web design basics"],
        "Future Occupation": [
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Web Developer"]
    },
    "Cybersecurity": {
        "study": [
            "Computer networks and OS basics",
            "Linux commands and system security basics",
            "Common attacks (phishing, malware, SQL injection)"],
        "Future Occupation": [
            "Cybersecurity Analyst",
            "Ethical Hacker",
            "Security Engineer"]
    },
    "Data Science": {
        "study": [
            "Python, statistics, and data analysis",
            "Pandas, NumPy, and data visualization",
            "Basic machine learning algorithms"],
        "Future Occupation": [
            "Data Analyst",
            "Data Scientist",
            "Business Intelligence Engineer"]
    },
    "UI/UX Design": {
        "study": [
            "Design principles and color theory",
            "Wire framing tools (Figma, Adobe XD basics)",
            "User research and usability testing"],
        "Future Occupation": [
            "UI Designer",
            "UX Designer",
            "Product Designer"]
    },
    "Cloud & Devops": {
        "study": [
            "Basics of Linux and command line",
            "Intro to cloud platforms (AWS, Azure, GCP)",
            "Version control (Git) and CI/CD basics"],
        "Future Occupation": [
            "Cloud Engineer",
            "Devops Engineer",
            "Site Reliability Engineer"]
    }
}
# Helper: get 0/1 safely
def ask_yes_no(question):
    while True:
        ans = input(question + " ")
        if ans in ["0", "1"]:
            return int(ans)
        print("Please enter only 1 for Yes or 0 for No.")
        
# 6 short questions
q1 = ask_yes_no("Do you enjoy solving logical or math problems? (1/0)")
if q1==1:
    scores["AI & Machine Learning"] += 2
    scores["Data Science"] += 2
    scores["Cybersecurity"] += 1

q2 = ask_yes_no("Do you like creating or designing visually appealing things? (1/0)")
if q2==1:
    scores["UI/UX Design"] += 2
    scores["Web Development"] += 1

q3 = ask_yes_no("Are you curious about how websites and apps are built? (1/0)")
if q3==1:
    scores["Web Development"] += 2
    scores["Cloud & Devops"] += 1

q4 = ask_yes_no("Do you like finding patterns in data or charts? (1/0)")
if q4==1:
    scores["Data Science"] += 2
    scores["AI & Machine Learning"] += 1

q5 = ask_yes_no("Are you interested in protecting systems from hackers? (1/0)")
if q5==1:
    scores["Cybersecurity"] += 2
    scores["Cloud & Devops"] += 1

q6 = ask_yes_no("Do you enjoy working with tools, automation, or cloud platforms? (1/0)")
if q6==1:
    scores["Cloud & Devops"] += 2
    scores["AI & Machine Learning"] += 1

# Find best paths
max_score = max(scores.values())
best_paths = [name for name, val in scores.items() if val==max_score]

# Interest level
if max_score <= 2:
    interest_level = "Low – You are still exploring different areas."
elif max_score <= 4:
    interest_level = "Medium – This area matches some of your interests."
else:
    interest_level = "High – This area strongly matches your interests!"

print("\n===== Result =====\n")

if len(best_paths)==1:
    print("Your Recommended Career Path is:")
else:
    print("You match well with multiple career paths:")

for path in best_paths:
    print("->", path)

print("\nInterest level:",interest_level)

print("\nScores for reference:")
for name,val in scores.items():
    print(f"{name}:{val}")

# Show what to study and future options for each best path
print("\n===== What You Should Study & Future Options =====\n")

for path in best_paths:
    info = study_plan[path]
    print("Career Path:", path)
    print("What you should study first:")
    for item in info["study"]:
        print(" -", item)
    print("Future career options:")
    for job in info["Future Occupation"]:
        print(" -", job)
    print()  # blank line between paths

print("Note:This is a simple guide. Explore online courses and resources for deeper learning")