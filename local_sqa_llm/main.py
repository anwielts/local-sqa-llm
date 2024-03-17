import argparse

import ollama


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model", nargs="*")
    parser.add_argument("output_dest", nargs="*")
    args = parser.parse_args()

    print(args)

    
if __name__ == "__main__":
    main()
