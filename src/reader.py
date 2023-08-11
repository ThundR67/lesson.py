"""Reader for the markdown script."""
import marko

from script import Script, Chapter


class Reader:
    def __init__(self, filename):
        self.filename = filename

    def parse_script(self):
        script = Script([])
        with open(self.filename, "r") as file:
            current_chapter = Chapter("", "", "")
            currently_reading_code = False
            for line in file.readlines():
                if line.startswith("```"):
                    currently_reading_code = not currently_reading_code
                elif currently_reading_code:
                    current_chapter.code += line
                elif line.startswith("#"):
                    if current_chapter.title != "":
                        script.chapters.append(current_chapter)
                        current_chapter = Chapter("", "", "")
                    current_chapter.title = line[1:].strip()
                else:
                    current_chapter.description += line

        return script


if __name__ == "__main__":
    reader = Reader("example.md")
    print(reader.parse_script())
