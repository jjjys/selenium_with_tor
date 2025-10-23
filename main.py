import undetected_chromedriver as uc
from selenium import webdriver
import subprocess
import atexit

def open_browser_with_tor():
    # Tor 프록시 설정
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
    chrome_options.add_argument('--incognito')

    # undetected-chromedriver로 브라우저 실행
    driver = uc.Chrome(options=chrome_options, headless=False)

    # 브라우저가 열려 있도록 유지
    return driver

def run_tor_background():
    """
    현재 프로젝트 디렉토리에서 tor.exe를 백그라운드로 실행하는 함수
    """
    try:
        # tor.exe를 백그라운드에서 실행
        process = subprocess.Popen(
            ["tor.exe"],
            cwd=".",  # 현재 디렉토리에서 실행
            stdout=subprocess.DEVNULL,  # 출력 숨김
            stderr=subprocess.DEVNULL
        )

        # 프로그램 종료 시 Tor 프로세스를 종료하도록 등록
        atexit.register(lambda: terminate_tor_process(process))
        return process
    except FileNotFoundError:
        print("tor.exe 파일을 찾을 수 없습니다. 프로젝트 디렉토리에 tor.exe가 있는지 확인하세요.")
        return None

def terminate_tor_process(process):
    """
    Tor 프로세스를 종료하는 함수
    """
    if process.poll() is None:  # 프로세스가 실행 중인지 확인
        process.terminate()
        print("Tor 프로세스를 종료했습니다.")
    # 터미널에서 제대로 종료되었는지 확인하려면 아래 명령어 사용
    # tasklist | findstr tor.exe

if __name__ == "__main__":
    # Tor 백그라운드 실행
    tor_process = run_tor_background()
    if tor_process is not None:
        print("Tor가 백그라운드에서 실행 중입니다.")

    driver = open_browser_with_tor()
    try:
        # 브라우저가 열려 있는 동안 대기
        driver.get("https://icanhazip.com")
        driver.get("http://check.torproject.org")
        input("브라우저를 닫으려면 Enter를 누르세요...")
    finally:
        driver.quit()
        if tor_process is not None:
            terminate_tor_process(tor_process)