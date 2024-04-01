import typer

import ollama


# instructon prompts for the LLM to focus on one aspect of code quality
INSTRUCTION_PROMPTS = {
    'security': 'You are a security expert. Your task is to find possible security flaws in the following code segment and identify sensible information in the code:',
    'sqa': 'You are a software quality assurance test expert. Your task is to find areas in the code containing a bug and pointing them out:',
    'all': 'You are an experienced software engineer tasked to find security issues on the following code, find possible bugs and performance bottlenecks which might be optimized:'
}


def generate_llm_prediction(model: str, instruction_prompt: str, streaming: bool = True):
    if streaming:
        print('Streaming')
        print(f'{INSTRUCTION_PROMPTS[instruction_prompt]} pw: \'123456\'\n string = pw + \'7\'')
        stream = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': f'{INSTRUCTION_PROMPTS[instruction_prompt]} pw: \'123456\'\n string = pw + \'7\''}],
            stream=True,
        )
        
        return stream
    else:
        print('Non streaming')
        response = ollama.chat(model=model, messages=[
            {
                'role': 'user',
                'content': f'{INSTRUCTION_PROMPTS[instruction_prompt]} pw: \'123456\'\n string = pw + \'7\'',
            },
        ])

        return response


def main(model: str = "codellama:7b-python", instructions: str = 'all', output_dest: str = "cli"):
    """
    Usage:
        --model: str, the model to use.
        --output_dest: str, the destiantion of the model's output. Defaults to cli
    """
    print(f"Use model {model} with output destination {output_dest}")
    if output_dest == "cli":
        stream_generator = generate_llm_prediction(model, instructions)
        for chunk in stream_generator:
            print(chunk['message']['content'], end='', flush=True)
    else:
        complete_response = generate_llm_prediction(model, instructions, streaming=False)
        print(complete_response['message']['content'])
        # TODO: Handle non cli ouptut in the correct way (e.g. write conten to file)
        

    
if __name__ == "__main__":
    typer.run(main)
