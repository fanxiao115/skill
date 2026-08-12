import os


REQUIRED_SECTIONS = [
    "Purpose",
    "Use Cases",
    "Input",
    "Workflow",
    "Output",
    "Safety Guidelines",
]


def validate_skill(path):
    with open(path, "r", encoding="utf-8") as file:
        content = file.read().lower()

    missing = []

    for section in REQUIRED_SECTIONS:
        if section.lower() not in content:
            missing.append(section)

    return missing


def main():

    skill_root = "skills"

    failed = False

    for root, dirs, files in os.walk(skill_root):

        for file in files:

            if file == "SKILL.md":

                path = os.path.join(root, file)

                missing = validate_skill(path)

                if missing:
                    failed = True

                    print(
                        f"❌ {path}"
                    )

                    print(
                        "Missing:",
                        missing
                    )

                else:
                    print(
                        f"✅ {path}"
                    )

    if failed:
        exit(1)

    print(
        "All skills passed validation."
    )


if __name__ == "__main__":
    main()
