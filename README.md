# Selenium with Tor

This project demonstrates how to use Selenium with Tor to browse the web anonymously. It includes functionality for running multiple Tor instances and configuring Selenium WebDriver to use different Tor proxies.

## Features

- **Single Tor Instance**: Run a single Tor instance in the background and configure Selenium to use it.
- **Multiple Tor Instances**: Run multiple Tor instances on different ports with separate data directories.
- **IP Check**: Verify the IP address used by each Tor instance using Naver's "My IP" search.
- **Automatic Cleanup**: Ensure Tor processes are terminated when the program exits.

## Prerequisites

1. **Python**: Install Python 3.7 or higher.
2. **Selenium**: Install the Selenium library.
3. **undetected-chromedriver**: Install the `undetected-chromedriver` library.
4. **Tor**: Ensure `tor.exe` is available in the project directory.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/jjjys/selenium_with_tor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd selenium_with_tor
   ```
3. Install the required Python libraries:
   ```bash
   pip install selenium undetected-chromedriver
   ```

## Usage

### Single Tor Instance

1. Run the script:
   ```bash
   python main.py
   ```
2. The script will launch a browser configured to use a single Tor instance.

### Multiple Tor Instances

1. Modify the `main.py` script to use the `run_m_tor_background` function.
2. Run the script:
   ```bash
   python main.py
   ```
3. The script will launch multiple browsers, each configured to use a different Tor instance.

### Check IP Address

The script includes functionality to check the IP address used by each Tor instance. It uses Naver's "My IP" search to display the IP address in the browser.

## File Structure

```
selenium_with_tor/
├── main.py          # Main script
├── readme.md        # Project documentation
├── tor_data1/       # Data directory for Tor instance 1
├── tor_data2/       # Data directory for Tor instance 2
├── tor_data3/       # Data directory for Tor instance 3
├── tor_data4/       # Data directory for Tor instance 4
```

## Demo Video

Check out the demo video for this project:
[![Selenium with Tor Demo](https://img.youtube.com/vi/uTADimuEYwE/0.jpg)](https://youtu.be/uTADimuEYwE)

## Notes

- Ensure `tor.exe` is in the project directory.
- Use `tasklist | findstr tor.exe` in the command line to check if Tor is running.
- The script automatically terminates Tor processes when the program exits.

## License

This project is licensed under the MIT License.
