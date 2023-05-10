import platform
import re


def palindrom(text):
    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]

    words = text.split()
    words = [word.strip(".,!?") for word in words]

    palindromes = [word for word in words if is_palindrome(word)]

    return palindromes


def validate_ip(ip_address):
    ip_regex = re.compile(
        r'^'
        r'(\d{1,3})\.'
        r'(\d{1,3})\.'
        r'(\d{1,3})\.'
        r'(\d{1,3})'
        r'$'
    )

    if not ip_regex.match(ip_address):
        return False

    octets = ip_address.split('.')
    for octet in octets:
        if not 0 <= int(octet) <= 255:
            return False

    return True


def get_os():
    os_name = platform.system()
    if os_name == "Darwin":
        return "Mac"
    elif os_name == "Windows":
        return "Windows"
    elif os_name == "Linux":
        return "Linux"
    else:
        return "Unknown OS"


