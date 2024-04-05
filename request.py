import requests
import sys

def send_request(success_condition, expected_value):
    try:
        # Send POST request
        response_post = requests.post(url, headers=headers, data=payload)

         # Check if the success condition is based on status code
        if success_condition == 'status-code':
            if response_post.status_code == int(expected_value):
                print("Request sent successfully.")
            else:
                print(f"Failed to send the request. Expected status code: {expected_value}, Actual status code:", response_post.status_code)

        # Check if the success condition is based on response body
        elif success_condition == 'response-body':
            if expected_value in response_post.text:
                print("Request sent successfully.")
            else:
                print("Failed to send request. Expected content not found in response body.")

        else:
            print("Invalid success condition provided.")

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: py request.py <URL> <num_runs> <headers_file> <payload_file> <success_condition> <expected_value>")
        sys.exit(1)

    url = sys.argv[1] # URL of the endpoint to sent requests to
    num_runs = int(sys.argv[2]) # Number of times to run the script
    headers_file = sys.argv[3] # Path to the file containing the header file (key/value pairs)
    payload_file = sys.argv[4] # Path to the file containing the payload information (form data)
    success_condition = sys.argv[5] # Condition for a successful request, either status-code or response-body
    expected_value = sys.argv[6] # The expected value for the success condition



    # Read headers from the headers file
    headers = {}
    with open(headers_file, 'r') as f:
        for line in f:
            key, value = line.strip().split(': ', 1)
            headers[key] = value

    payload = {}
    with open(payload_file, 'r') as f:
        for line in f:
            key, value = line.strip().split(': ', 1)
            payload[key] = value
    

    # Print tests for headers/payload
#    print("Parsed payloads:")
#    for key, value in payload.items():
#        print(f"{key}: {value}")


    # Loop to run the script multiple times
    for i in range(num_runs):
        print(f"Running iteration {i+1}/{num_runs}")
        send_request(success_condition, expected_value)

