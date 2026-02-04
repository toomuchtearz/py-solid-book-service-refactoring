from app.book import Book
from app.services.display import ConsoleDisplay, ReverseDisplay
from app.services.printer import ConsolePrinter, ReversePrinter
from app.services.serializer import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    serializer_mapping = {
        "json": JSONSerializer,
        "xml": XMLSerializer,
    }
    printer_mapping = {
        "console": ConsolePrinter,
        "reverse": ReversePrinter,
    }
    display_mapping = {
        "console": ConsoleDisplay,
        "reverse": ReverseDisplay,
    }

    for command, process_type in commands:
        if command == "serialize":
            serializer = serializer_mapping.get(process_type)()
            return serializer.serialize(book=book)
        elif command == "print":
            printer = printer_mapping.get(process_type)()
            printer.print(book=book)
        elif command == "display":
            display = display_mapping.get(process_type)()
            display.display(book=book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    main(
        sample_book,
        [
            ("serialize", "json"),
        ],
    )
