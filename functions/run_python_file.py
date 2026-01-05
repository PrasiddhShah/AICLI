import os
import subprocess
from google.genai import types
def run_python_file(working_directory, file_path, args=None):
    try:
        absPath = os.path.abspath(working_directory)
        targetDir = os.path.normpath(os.path.join(absPath,file_path))
        if os.path.commonpath([absPath,targetDir]) != absPath:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(targetDir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not targetDir.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", targetDir]
        if args:
            command.extend(args)
        result= subprocess.run(
            command,
            cwd=absPath,
            capture_output=True,
            text=True,
            timeout=30
            )
        processOutput =[]
        if result.returncode !=0:
            processOutput.append(f"Process exited with code {result.returncode}")
        if not result.stderr and not result.stdout:
            processOutput.append(f"No output produced")
        if result.stdout:
            processOutput.append(f"STDOUT: {result.stdout}")
        if result.stderr:
            processOutput.append(f"STDERR: {result.stderr}")
        return "\n".join(processOutput)

    except Exception as e:
        return f"Error: executing python file: {e}"
    
def run_python_schema():
    schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Executes a Python file within the working directory and returns its output (stdout, stderr, and exit code if non-zero)",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="Path to the Python file to execute, relative to the working directory",
                ),
                "args": types.Schema(
                    type=types.Type.ARRAY,
                    items=types.Schema(type=types.Type.STRING),
                    description="Optional command line arguments to pass to the Python script",
                ),
            },
            required=["file_path"],
        ),
    )
    return schema_run_python_file