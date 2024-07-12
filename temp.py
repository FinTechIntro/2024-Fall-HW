import sys
import re
import requests

def create_github_comment(repo, token, comment):
    url = f"https://api.github.com/repos/{repo}/issues"
    # /repos/{owner}/{repo}/issues
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    data = {
        "body": comment,
        "title": "Homework",
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print("Comment created successfully!")
    else:
        print(f"Failed to create comment: {response.status_code}")
        print(response.json())

def extract_test_results(line):
    # Define a regex pattern to extract the test results
    pattern = r"(\d+) tests passed, (\d+) failed, (\d+) skipped \((\d+) total tests\)"
    match = re.search(pattern, line)
    
    if match:
        passed = match.group(1)
        failed = match.group(2)
        skipped = match.group(3)
        total = match.group(4)
        return passed, failed, skipped, total
    else:
        return None, None, None, None

def main():
    if len(sys.argv) < 4:
        print("Usage: your_script.py <last_line_of_output>")
        sys.exit(1)

    last_line = sys.argv[1]
    repo = sys.argv[2]
    token = sys.argv[3]
    passed, failed, skipped, total = extract_test_results(last_line)
    comment = f'Tests passed {passed} Total Failed {failed} Score: {10 * int(passed)}'
    create_github_comment(repo, token, comment)
    
    if passed is not None:
        print(f"Tests passed: {passed}")
        print(f"Tests failed: {failed}")
        print(f"Tests skipped: {skipped}")
        print(f"Total tests: {total}")
    else:
        print("Failed to parse the test results.")

if __name__ == "__main__":
    main()
