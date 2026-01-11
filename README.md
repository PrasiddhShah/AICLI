# AICLI

An AI-powered command-line interface agent that uses Google's Gemini API to execute tasks on your local system. The agent can explore files, read/write content, and execute Python scripts through natural language commands.

## Features

- **File Exploration** - List files and directories with metadata
- **File Reading** - Read file contents with automatic truncation
- **File Writing** - Create or overwrite files with automatic directory creation
- **Python Execution** - Run Python scripts with arguments and capture output
- **Agentic Loop** - Multi-turn conversation with the Gemini model
- **Security Sandbox** - All file operations are confined to a working directory

## Requirements

- Python 3.13+
- Google Gemini API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd AICLI
```

2. Install dependencies using uv:
```bash
uv sync
```

Or using pip:
```bash
pip install google-genai python-dotenv
```

3. Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

### Basic Usage

```bash
python main.py "your query here"
```

### With Verbose Output

```bash
python main.py --verbose "your query here"
```

### Examples

```bash
# List files in a directory
python main.py "List the files in the calculator directory"

# Read a file
python main.py "Read the calculator tests"

# Run a Python script
python main.py "Run 3 + 5 using the calculator"

# Create a file
python main.py "Create a file named example.txt with Hello World"
```

## Project Structure

```
AICLI/
├── main.py                 # Entry point for the CLI agent
├── config.py               # Configuration constants
├── prompts.py              # System prompt for the AI agent
├── call_function.py        # Function call router
├── functions/              # Core function implementations
│   ├── get_files_info.py   # List files/directories
│   ├── get_file_content.py # Read file contents
│   ├── write_file.py       # Create/write files
│   └── run_python_file.py  # Execute Python scripts
├── calculator/             # Demo calculator application
│   ├── main.py             # Calculator entry point
│   ├── tests.py            # Unit tests
│   └── pkg/
│       ├── calculator.py   # Expression evaluator
│       └── render.py       # Output formatter
└── test_*.py               # Integration tests
```

## Running Tests

```bash
# Calculator unit tests
python calculator/tests.py

# Integration tests
python test_get_files_info.py
python test_get_file_content.py
python test_write_file.py
python test_run_python_file.py
```

## Configuration

| Setting | Location | Description |
|---------|----------|-------------|
| `MAX_CHARS` | `config.py` | Maximum characters to read from files (default: 1000) |
| `GEMINI_API_KEY` | `.env` | Your Google Gemini API key |
| Working Directory | `call_function.py` | Sandbox directory for file operations |

## How It Works

1. User provides a natural language prompt via CLI
2. The agent sends the prompt to Google's Gemini 2.5 Flash model
3. Gemini may request function calls (file operations, script execution)
4. The agent executes the requested function and returns results
5. This loop continues until Gemini provides a final text response
6. Maximum of 20 iterations to prevent infinite loops

## License

MIT
