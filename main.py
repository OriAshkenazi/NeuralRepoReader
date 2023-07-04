from nrr.library import Library

lib = Library("NeuralRepoReader", "https://github.com/OriAshkenazi/NeuralRepoReader")
ov = lib.get_overview()

print(ov)