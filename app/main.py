from app.book import Book
from app.services.display import Display
from app.services.printer import Printer
from app.services.serializer import Serializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for command, process_type in commands:
        if command == "display":
            Display.print(
                book=book,
                display_type=process_type
            )
        elif command == "print":
            Printer.print(
                book=book,
                print_type=process_type
            )
        elif command == "serialize":
            return Serializer.serialize(
                book=book,
                serialize_type=process_type
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    main(
        sample_book,
        [
            ("serialize", "json"),
        ],
    )
