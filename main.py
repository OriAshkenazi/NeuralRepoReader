from nrr.library import Library

lib = Library("gpt-engineer", "https://github.com/AntonOsika/gpt-engineer.git")
ov = lib.get_overview()

print(ov)