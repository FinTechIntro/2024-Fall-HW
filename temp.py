import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: your_script.py <last_line_of_output>")
        sys.exit(1)

    last_line = sys.argv[1]
    print(f"Last line of output: {last_line}")

if __name__ == "__main__":
    main()
