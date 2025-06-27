import subprocess
import sys

def execute_command(command, capture_output=True, text=True, check=False):
    try:
        result = subprocess.run(
            command,
            capture_output=capture_output,
            text=text,
            check=check,
            shell=isinstance(command, str)
        )
        return result

    except subprocess.CalledProcessError as e:
        print(f"{e}")

    except FileNotFoundError:
        print(f"Error: Command {command} not found. Makse sure it is in your server")


def main():
    print("---Sytem Command Executor--")
    if sys.platform.startswith('win'):
        list_command = "dir"
    else:
        list_command = ["ls", "-l"]

    result = execute_command(list_command)
    if result and result.returncode == 0:
        print("Command executed sucessfully. output:")
        print(result.stdout)
    elif result:
        print(f"Command failed with exit code: {result.returncode}")
        print(f"Sterr: {result.stderr}")


if __name__ == "__main__":
    main()

    
