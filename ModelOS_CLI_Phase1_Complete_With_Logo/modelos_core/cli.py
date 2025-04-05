import typer
import json
from modelos_core.mcp.schema import MCPContext
from openai import OpenAI
import datetime
import subprocess
import os

app = typer.Typer()

@app.command()
def run(
    prompt: str = typer.Option(None, help="Text prompt for the model"),
    audio: str = typer.Option(None, help="Optional audio file to transcribe"),
    model: str = "gpt-4",
    temperature: float = 0.7,
):
    """Run the model with MCP logging. Supports text or audio input."""
    if audio:
        print("Transcribing audio using Whisper...")
        try:
            result = subprocess.run(
                ["whisper", audio, "--model", "base", "--output_format", "txt"],
                check=True,
                capture_output=True,
                text=True
            )
            with open(audio.replace(".wav", ".txt")) as f:
                prompt = f.read()
        except Exception as e:
            typer.echo(f"Error transcribing audio: {e}")
            raise typer.Exit()

    if not prompt:
        typer.echo("Please provide a text prompt or an audio file.")
        raise typer.Exit()

    # Build MCP context
    context = MCPContext(
        user_input=prompt,
        model_name=model,
        temperature=temperature
    )

    # Initialize OpenAI client
    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": context.system_prompt},
            {"role": "user", "content": context.user_input}
        ],
        temperature=temperature
    )

    output = response.choices[0].message.content
    context.output = output

    # Display output
    print("\nAI Response:\n" + output)

    # Save to MCP log
    timestamp = datetime.datetime.utcnow().isoformat()
    log_dir = "mcp_logs"
    os.makedirs(log_dir, exist_ok=True)
    with open(os.path.join(log_dir, f"log_{timestamp}.json"), "w") as f:
        json.dump(context.dict(), f, indent=2)

if __name__ == "__main__":
    app()
