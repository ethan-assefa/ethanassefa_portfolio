# convert_conda_to_pip.py
conda_file = "env-spec.txt"
pip_file = "env-pip-spec.txt"

with open(conda_file, "r") as infile, open(pip_file, "w") as outfile:
    for line in infile:
        if line.strip() and not line.startswith("#"):
            parts = line.split()
            pkg = parts[0]
            version = parts[1] if len(parts) > 1 else ""
            if version:
                outfile.write(f"{pkg}=={version}\n")
            else:
                outfile.write(f"{pkg}\n")