def parse_pep(s):
    intro, body = s.split("\n\n", 1)
    pep = {}
    current_key = None
    current_value = None
    for line in intro.split("\n"):
        # If the line starts with whitespace, it's a continuation of the previous value
        if line.startswith(" ") or line.startswith("\t"):
            if current_key is not None:
                current_value += " " + line.strip()
                pep[current_key] = current_value.strip()
        else:
            # Split the line into key and value
            parts = line.split(": ", 1)
            if len(parts) == 2:
                key, value = parts
                # Update the current key and value
                current_key = key
                current_value = value
                # Add the key-value pair to the pep dictionary
                pep[current_key] = current_value.strip()
    pep["Body"] = body.strip()
    return pep