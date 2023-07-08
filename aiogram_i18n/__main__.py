import argparse
from typing import List, Dict, Callable
from pathlib import Path


def stub(input_files: List[str], output_file: str):
    from aiogram_i18n.utils.fluent_stub import from_files_to_file
    allow_formats: Dict[str, Callable[[List[str], str], None]] = {
        "ftl": from_files_to_file,
        # "mo"
    }
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
    allow_formats[suffix](input_files, output_file) # noqa


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help='Command to run', choices=['stub'])
    parser.add_argument('-i', '--input', nargs='+', help='Input files')
    parser.add_argument('-o', '--output', nargs=1, help='Output file')
    args = parser.parse_args()

    if args.command == "stub":
        stub(input_files=args.input, output_file=args.output[0])


if __name__ == '__main__':
    main()
