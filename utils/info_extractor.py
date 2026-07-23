import re


def extract_info(text):

    info = {
        "name": "",
        "email": "",
        "phone": "",
        "linkedin": "",
        "github": ""
    }

    # Email
    email = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    if email:
        info["email"] = email.group()

    # Phone Number
    phone = re.search(
        r"(\+91[\-\s]?)?[6-9]\d{9}",
        text
    )

    if phone:
        info["phone"] = phone.group()

    # LinkedIn
    linkedin = re.search(
        r"(https?://)?(www\.)?linkedin\.com/[^\s]+",
        text,
        re.IGNORECASE
    )

    if linkedin:
        info["linkedin"] = linkedin.group()

    # GitHub
    github = re.search(
        r"(https?://)?(www\.)?github\.com/[^\s]+",
        text,
        re.IGNORECASE
    )

    if github:
        info["github"] = github.group()

    # Name (First non-empty line)
    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) > 2:

            info["name"] = line

            break

    return info