def summarize_note(note, max_sentences=2):
    sentences = note.split(".")
    summary = []

    for sentence in sentences:
        sentence = sentence.strip()

        if sentence != "":
            summary.append(sentence)

        if len(summary) == max_sentences:
            break

    return ". ".join(summary) + "."


def extract_keywords(note):
    basic_keywords = [
        "biology",
        "neuroscience",
        "bioinformatics",
        "data",
        "machine learning",
        "brain",
        "computational biology"
    ]

    found_keywords = []
    lower_note = note.lower()

    for keyword in basic_keywords:
        if keyword in lower_note:
            found_keywords.append(keyword)

    return found_keywords


def main():
    sample_note = """
    Bio and brain engineering connects biology, neuroscience, and engineering.
    Students in this field often study biological systems using data analysis and computational tools.
    This project aims to support beginner-friendly scientific learning through simple code examples.
    """

    summary = summarize_note(sample_note)
    keywords = extract_keywords(sample_note)

    print("Summary:")
    print(summary)

    print()
    print("Keywords:")
    print(keywords)


if __name__ == "__main__":
    main()
