import wikipedia


def search_wikipedia():
    while True:
        title = input("Enter page title: ")
        if not title:
            print("Thank you.")
            break

        try:
            page = wikipedia.page(title)
            print(f"\n{page.title}\n{page.summary[:500]}...\n{page.url}\n")

        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except wikipedia.PageError:
            # Handle cases where the page does not exist
            print(f'Page "{title}" does not match any pages. Try another title!')

        except wikipedia.exceptions.WikipediaException as e:
            # Handle any other Wikipedia-related exceptions
            print(f"An error occurred: {e}")


if __name__ == '__main__':
    search_wikipedia()
