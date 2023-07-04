from nrr.library import Library

lib = Library("NeuralRepoReader", "https://github.com/OriAshkenazi/NeuralRepoReader.git")
ov = lib.get_overview()

print(ov)