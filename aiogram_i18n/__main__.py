
from pathlib import Path
from typing import Dict, Callable, Tuple, Sequence

import click


@click.group(name="main")
def main() -> None:
    ...


@main.command(help="Generate stubs from .ftl files")  # type: ignore[arg-type]
@click.option("-i", "--input-files", required=True, multiple=True)
@click.option("-o", "--output-file", required=True)
def stub(input_files: Tuple[str, ...], output_file: str) -> None:
    from aiogram_i18n.utils.fluent_stub import from_files_to_file

    allow_formats: Dict[str, Callable[[Sequence[str], str], None]] = {
        "ftl": from_files_to_file,
        # "mo"
    }

    suffix: str = "ftl"
    for input_file in input_files:
        path = Path(input_file)
        suffix = path.suffix[1:]
        if not suffix:
            raise Exception(f"only files with this extension are allowed ({', '.join(allow_formats.keys())})")
        if suffix not in allow_formats:
            raise Exception(f"unknown file extension {path.suffix}")
        if not path.is_file():
            raise Exception("only files allowed")

    path = Path(output_file)
    if path.suffix != ".pyi":
        raise Exception('output file must have the extension "pyi"')

    allow_formats[suffix](input_files, output_file)


@main.command(help="Extract all used fluent keys from code")  # type: ignore[arg-type]
@click.option("-i", "--input-dirs", required=True, multiple=True)
@click.option("-o", "--output-file", required=True)
@click.option("-k", "--i18n-keys", default=["i18n", "L"], multiple=True, show_default=True)
@click.option("-s", "--separator", default="-", show_default=True)
@click.option("-ed", "--exclude-dirs", default=["venv"], multiple=True)
@click.option("-ek", "--exclude-keys", multiple=True)
def extract(
    input_dirs: Tuple[str, ...], output_file: str,
    i18n_keys: Tuple[str, ...], separator: str,
    exclude_dirs: Tuple[str, ...], exclude_keys: Tuple[str, ...]
) -> None:
    from aiogram_i18n import I18nContext
    from aiogram_i18n.utils.fluent_extract import FluentKeyParser

    exclude_dirs += "__pycache__",
    exclude_keys += tuple(
        key for key, value in I18nContext.__dict__.items() if callable(value)
    )

    fkp = FluentKeyParser(
        input_dirs=input_dirs,
        output_file=output_file,
        i18n_keys=i18n_keys,
        separator=separator,
        exclude_dirs=exclude_dirs,
        exclude_keys=exclude_keys
    )
    fkp.run()


if __name__ == '__main__':
    main()
