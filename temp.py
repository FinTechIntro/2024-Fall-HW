import sys
import re
import requests

def create_github_commit_comment(repo, commit_sha, token):
    url = f"https://api.github.com/repos/{repo}/commits/{commit_sha}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "body": "Hi"
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
    if len(sys.argv) < 5:
        print("Usage: your_script.py <last_line_of_output>")
        sys.exit(1)

    last_line = sys.argv[1]
    repo = sys.argv[1]
    commit_sha = sys.argv[2]
    token = sys.argv[3]
    create_github_commit_comment(repo, commit_sha, token)
    passed, failed, skipped, total = extract_test_results(last_line)
    
    if passed is not None:
        print(f"Tests passed: {passed}")
        print(f"Tests failed: {failed}")
        print(f"Tests skipped: {skipped}")
        print(f"Total tests: {total}")
    else:
        print("Failed to parse the test results.")

if __name__ == "__main__":
    main()
