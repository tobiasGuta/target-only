from urllib.parse import urlparse

# Function to check if a URL belongs to a specific subdomain
def is_valid_subdomain(url, subdomain):
    parsed_url = urlparse(url)
    if parsed_url.hostname:
        # Extract the hostname (domain) from the URL
        hostname = parsed_url.hostname
        # Check if the hostname matches the specific subdomain
        if hostname.endswith(subdomain) or hostname.endswith('.' + subdomain):
            return True
    return False

def filter_urls(input_file, output_file, subdomain):
    with open(input_file, 'r') as f_in:
        urls = f_in.read().splitlines()

    valid_urls = []
    invalid_urls = []

    for url in urls:
        if is_valid_subdomain(url, subdomain):
            valid_urls.append(url)
        else:
            invalid_urls.append(url)

    with open(output_file, 'w') as f_out:
        for url in valid_urls:
            f_out.write(url + '\n')

    print(f"Valid URLs for subdomain '{subdomain}' (saved to '{output_file}'):")
    for url in valid_urls:
        print(url)

    print("\nInvalid URLs:")
    for url in invalid_urls:
        print(url)

# Example usage:
input_file = 'endpoint.txt'  #change this
output_file = 'valid_urls.txt'  #change this
subdomain = 'globe.gov'    #change this

filter_urls(input_file, output_file, subdomain)
