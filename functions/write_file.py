import os
from google.genai import types
def write_file(working_directory,file_path, content):
    try:
        absPath = os.path.abspath(working_directory)
        targetDir = os.path.normpath(os.path.join(absPath,file_path))
        if os.path.commonpath([absPath,targetDir]) != absPath:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(targetDir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        parentDir = os.path.dirname(targetDir)
        os.makedirs(parentDir, exist_ok=True)
        with open(targetDir,"w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

def write_file_schema():
    schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Creates or overwrites a file with the specified content. Parent directories are created automatically if they don't exist. Returns the number of characters written.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="Path to the file to write, relative to the working directory",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The text content to write to the file",
                ),
            },
            required=["file_path", "content"],
        ),
    )
    return schema_write_file