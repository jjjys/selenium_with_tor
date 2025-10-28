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

def open_browser_with_m_tor(port):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--proxy-server=socks5://127.0.0.1:{port}')
    chrome_options.add_argument('--incognito')
    return uc.Chrome(options=chrome_options, headless=False)

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

def run_m_tor_background(port, data_dir):
    """
    지정한 포트와 데이터 디렉토리로 tor.exe 실행
    """
    try:
        process = subprocess.Popen(
            [
                "tor.exe",
                f"--SocksPort", str(port),
                f"--DataDirectory", data_dir
            ],
            cwd=".",
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        atexit.register(lambda: terminate_tor_process(process))
        return process
    except FileNotFoundError:
        print("tor.exe 파일을 찾을 수 없습니다.")
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

def check_ip_with_naver(drv1,drv2,drv3,drv4):
    # 화면 세팅
    drv1.set_window_size(974, 527)
    drv2.set_window_size(974, 527)
    drv3.set_window_size(974, 527)
    drv4.set_window_size(974, 527)

    drv1.set_window_position(-7, 0)
    drv2.set_window_position(-7, 520)
    drv3.set_window_position(953, 0)
    drv4.set_window_position(953, 520)

    my_ip_naver_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%B4+%EC%95%84%EC%9D%B4%ED%94%BC&ackey=2o5cjxaq"
    drv1.get(my_ip_naver_url)
    drv2.get(my_ip_naver_url)
    drv3.get(my_ip_naver_url)
    drv4.get(my_ip_naver_url)

    
if __name__ == "__main__":
    # ##### [ 기존 단일 Tor 실행 코드 테스트 ] ##########################
    # # Tor 백그라운드 실행
    # tor_process = run_tor_background()
    # if tor_process is not None:
    #     print("Tor가 백그라운드에서 실행 중입니다.")

    # driver = open_browser_with_tor()
    # try:
    #     # 브라우저가 열려 있는 동안 대기
    #     driver.get("https://icanhazip.com")
    #     driver.get("http://check.torproject.org")
    #     input("브라우저를 닫으려면 Enter를 누르세요...")
    # finally:
    #     driver.quit()
    #     if tor_process is not None:
    #         terminate_tor_process(tor_process)

    # ##### [ 다중 Tor 실행 코드 테스트 ] ##########################
    check_my_ip = "https://icanhazip.com"
    
    # Tor 여러 개 실행
    tor1 = run_m_tor_background(9050, "tor_data1")
    tor2 = run_m_tor_background(9051, "tor_data2")
    tor3 = run_m_tor_background(9052, "tor_data3")
    tor4 = run_m_tor_background(9053, "tor_data4")

    # 각기 다른 포트로 드라이버 실행
    driver1 = open_browser_with_m_tor(9050)
    driver2 = open_browser_with_m_tor(9051)
    driver3 = open_browser_with_m_tor(9052)
    driver4 = open_browser_with_m_tor(9053)

    try:
        # driver1.get(check_my_ip)
        # driver2.get(check_my_ip)
        # driver3.get(check_my_ip)
        # driver4.get(check_my_ip)
        check_ip_with_naver(driver1,driver2,driver3,driver4)
        input("브라우저 닫으려면 Enter...")
    finally:
        driver1.quit()
        driver2.quit()
        driver3.quit()
        driver4.quit()
        terminate_tor_process(tor1)
        terminate_tor_process(tor2)
        terminate_tor_process(tor3)
        terminate_tor_process(tor4)
