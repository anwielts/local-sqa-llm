import typer

import ollama


def main(model: str, output_dest: str = "cli"):
    """
    Usage:
        --model: str, the model to use.
        --output_dets: str, the destiantion of the model's output. Defaults to cli
    """
    print(f"Use model {model} with output destination {output_dest}")

    
if __name__ == "__main__":
    typer.run(main)
