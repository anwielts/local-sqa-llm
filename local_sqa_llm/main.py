import typer

import ollama


def generate_llm_prediction(model: str, streaming: bool = True):
    if streaming:
        print('Streaming')
        stream = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
            stream=True,
        )
        
        return stream
    else:
        print('Non streaming')
        response = ollama.chat(model=model, messages=[
            {
                'role': 'user',
                'content': 'Why is the sky blue?',
            },
        ])

        return response


def main(model: str = "starcoder2:3b", output_dest: str = "cli"):
    """
    Usage:
        --model: str, the model to use.
        --output_dest: str, the destiantion of the model's output. Defaults to cli
    """
    print(f"Use model {model} with output destination {output_dest}")
    if output_dest == "cli":
        stream_generator = generate_llm_prediction(model)
        for chunk in stream_generator:
            print(chunk['message']['content'], end='', flush=True)
    else:
        complete_response = generate_llm_prediction(model, streaming=False)
        print(complete_response['message']['content'])
    

    
if __name__ == "__main__":
    typer.run(main)
