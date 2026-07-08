from bis_notes.summarizer import extract_keywords, summarize_note


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
