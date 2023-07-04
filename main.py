from nrr.library import Library
import logging

logging.basicConfig(filename='gpt4_calls.log', level=logging.INFO)

lib = Library("gpt-engineer", "https://github.com/AntonOsika/gpt-engineer.git")
ov = lib.get_overview()

print(ov)