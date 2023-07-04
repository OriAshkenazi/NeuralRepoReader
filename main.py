from nrr.library import Library

lib = Library("https://github.com/OriAshkenazi/NeuralRepoReader")
ov = lib.get_overview()

print(ov)