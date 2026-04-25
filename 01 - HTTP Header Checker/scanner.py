import requests
import argparse


def scan(url, output):
    security_headers = [
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Permissions-Policy",
        "Referrer-Policy",
    ]
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print(url, "could not be reached")
        return

    if output is not None:
        with open(output, "a") as f:
            f.write("\n")
            f.write("===============\n")
            f.write(url + "\n")
            f.write("===============\n")
            f.write(str(response.status_code) + "\n")
            f.write("\n")
            for header in security_headers:
                status = response.headers.get(header)
                if status is None:
                    f.write(header + " " + "MISSING" + "\n")
                else:
                    f.write(header + " " + status + "\n")

    print("\n")
    print("===============")
    print(url)
    print("===============")
    print("Status code ", response.status_code, "\n")

    for header in security_headers:
        status = response.headers.get(header)
        if status is None:
            print(header, "MISSING")
        else:
            print(header, status)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="With -u/--url you can pass a single URL")
    parser.add_argument(
        "-f", "--file", help="-f/--file allows you to use a .txt file to scan URLS "
    )
    parser.add_argument(
        "-o", "--output", help="Using this command allows you to save the output."
    )
    args = parser.parse_args()

    if args.url is None and args.file is None:
        print("Provide an URL with -u or -f.")
    elif args.url is not None:
        scan(args.url, args.output)
    else:
        with open(args.file, "r") as f:
            userlist = f.read().splitlines()
            if len(userlist) == 0:
                print("File is empty.")
                return
            for url in userlist:
                scan(url, args.output)


if __name__ == "__main__":
    main()
