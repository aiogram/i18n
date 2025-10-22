from collections.abc import Sequence

from click import echo, style


def from_files_to_file_ex(files: Sequence[str], to_file: str) -> None:  # noqa: ARG001
    echo(
        style(
            text="This function is removed. Use FTL-Extract instead.\n"
            "pip install ftl-extract\n"
            "\n"
            "ftl stub <locale_path> <stub_output_path>\n"
            "\n"
            "https://pypi.org/project/FTL-Extract/",
            fg="red",
        ),
        err=True,
        color=True,
    )
