import os
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
