def extract_skills(text):

    skills_database = [

        "python",
        "java",
        "c",
        "c++",
        "sql",
        "mysql",
        "html",
        "css",
        "javascript",
        "flask",
        "django",
        "react",
        "nodejs",
        "git",
        "github",
        "machine learning",
        "deep learning",
        "data science",
        "numpy",
        "pandas",
        "matplotlib",
        "tensorflow",
        "pytorch",
        "scikit-learn",
        "nlp",
        "opencv",
        "mongodb",
        "aws",
        "docker",
        "linux"
    ]

    text = text.lower()

    extracted_skills = []

    for skill in skills_database:

        if skill in text:

            extracted_skills.append(skill.title())

    return sorted(set(extracted_skills))