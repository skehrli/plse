import requests
import time
from bs4 import BeautifulSoup
from getpass import getpass


def login_to_github(session, username, password):
    login_url = 'https://github.com/login'
    response = session.get(login_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    authenticity_token = soup.find(
        'input', {'name': 'authenticity_token'})['value']

    login_payload = {
        'login': username,
        'password': password,
        'authenticity_token': authenticity_token
    }

    session.post(login_url, data=login_payload)


def get_search_results_count(session, search_term):
    try:
        url = f'https://github.com/search?q={search_term}+language%3AJava&type=code'
        response = session.get(url)
        while response.status_code == 429:
            wait_time = int(response.headers['Retry-After'])
            print(f"Rate limit exceeded. Waiting for {wait_time} seconds.")
            time.sleep(wait_time)
            response = session.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        result_count_element = soup.find(
            'div', class_='Box-sc-g0xbh4-0 cgQapc')

        if result_count_element:
            result_text = result_count_element.text.strip()
            result_count = float(result_text.split()[0].replace('k', ''))
            result_count = int(result_count * 1000)
            return result_count

    except requests.RequestException as e:
        print(f"Request failed: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

    return 0


# Prompt the user for GitHub credentials
# github_username = input("Enter your GitHub username: ")
# github_password = getpass("Enter your GitHub password: ")


def main():
    # Replace with your list of search terms
    github_username = "sascha.kehrli@gmail.com"
    github_password = "{IQc^i8M,5.6J0N\"OS<(]`!*"

    # Create a session and log in
    github_session = requests.Session()
    login_to_github(github_session, github_username, github_password)
    search_terms = [
        "AbstractInterruptibleChannel", "AbstractSelectableChannel", "AbstractSelector", "AsynchronousFileChannel", "AsynchronousServerSocketChannel", "AsynchronousSocketChannel", "AudioInputStream", "BufferedInputStream", "BufferedOutputStream", "BufferedReader", "BufferedWriter", "ByteArrayInputStream", "ByteArrayOutputStream", "CharArrayReader", "CharArrayWriter", "CheckedInputStream", "CheckedOutputStream", "CipherInputStream", "CipherOutputStream", "DatagramChannel", "DatagramSocket", "DataInputStream", "DataOutputStream", "DeflaterInputStream", "DeflaterOutputStream", "DigestInputStream", "DigestOutputStream", "FileCacheImageInputStream", "FileCacheImageOutputStream", "FileChannel", "FileImageInputStream", "FileImageOutputStream", "FileInputStream", "FileOutputStream", "FileReader", "FileSystem", "FileWriter", "FilterInputStream", "FilterOutputStream", "FilterReader", "FilterWriter", "Formatter", "ForwardingJavaFileManager", "GZIPInputStream", "GZIPOutputStream", "ImageInputStreamImpl", "ImageOutputStreamImpl", "InflaterInputStream", "InflaterOutputStream", "InputStream", "InputStream", "InputStream", "InputStreamReader", "JarFile", "JarInputStream", "JarOutputStream", "LineNumberInputStream", "LineNumberReader", "LogStream", "MemoryCacheImageInputStream", "MemoryCacheImageOutputStream", "MLet", "MulticastSocket", "ObjectInputStream", "ObjectOutputStream", "OutputStream", "OutputStream", "OutputStream", "OutputStreamWriter", "Pipe.SinkChannel", "Pipe.SourceChannel", "PipedInputStream", "PipedOutputStream", "PipedReader", "PipedWriter", "PrintStream", "PrintWriter", "PrivateMLet", "ProgressMonitorInputStream", "PushbackInputStream", "PushbackReader", "RandomAccessFile", "Reader", "RMIConnectionImpl", "RMIConnectionImpl_Stub", "RMIConnector", "RMIIIOPServerImpl", "RMIJRMPServerImpl", "RMIServerImpl", "Scanner", "SelectableChannel", "Selector", "SequenceInputStream", "ServerSocket", "ServerSocketChannel", "Socket", "SocketChannel", "SSLServerSocket", "SSLSocket", "StringBufferInputStream", "StringReader", "StringWriter", "URLClassLoader", "Writer", "ZipFile", "ZipInputStream", "ZipOutputStream"
    ]

    # for term in search_terms:
    #     result_count = get_search_results_count(github_session, term)
    #     print(f'Search term: {term}, Results count: {result_count}')


if __name__ == "__main__":
    main()
