import os
from google.genai import types
def get_files_info(working_directory,directory="."):
    try:
        absPath = os.path.abspath(working_directory)
        targetDir = os.path.normpath(os.path.join(absPath,directory))
        if os.path.commonpath([absPath,targetDir]) != absPath:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(targetDir):
            return f'Error: "{directory}" is not a directory'
        
        fileLs = os.scandir(targetDir)
        dirinfo =""
        for files in fileLs:
            dirinfo += f"\n- {files.name}: file_size={files.stat().st_size} bytes, is_dir={files.is_dir()}"
        return dirinfo.strip('\n')
    except Exception as e:
        return f"Error listing files: {e}"

def file_info_schema():
    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
                ),
            },
        ),
    )
    return schema_get_files_info
