# 🕷️ ScrapeSome

**ScrapeSome** is a lightweight, flexible web scraping library with both **synchronous** and **asynchronous** support. It includes intelligent fallbacks, JavaScript page rendering, response formatting (HTML → Text/JSON/Markdown), and retry mechanisms. Ideal for developers who need robust scraping utilities with minimal setup.

---

## 🚀 Features

- 🔁 Sync + Async scraping support
- 🔄 Automatic retries and intelligent fallbacks
- 🧪 Playwright rendering fallback for JS-heavy pages
- 📝 Format responses as raw HTML, plain **text**, **Markdown**, or structured **JSON**
- ⚙️ Configurable: timeouts, redirects, user agents, and logging
- 🧪 Test coverage with `pytest` and `pytest-asyncio`

---

## 📦 Installation

```bash
pip install scrapesome
```

## ⚡ Quick Start
Synchronous Example

```python
from scrapesome.scraper.sync_scraper import scraper
html = scraper("https://example.com")
html
```


Asynchronous Example

```python
import asyncio
from scrapesome.scraper.async_scraper import scraper
html = asyncio.run(scraper("https://example.com"))
html
```

## 🧰 Advanced Usage

Force Rendering (Playwright)

```python
from scrapesome.scraper.sync_scraper import scraper
content = scraper("https://example.com", force_playwright=True)
content
```

Custom User Agents

```python
from scrapesome.scraper.sync_scraper import scraper
content = scraper("https://example.com", user_agents=["MyCustomAgent/1.0"])
content
```

Control Redirects

```python
from scrapesome.scraper.sync_scraper import scraper
content = scraper("https://example.com", allow_redirects=False)
content
```

Similarly async can also be used.

## 🧪 Testing
Run tests with:

```bash
pytest --cov=scrapesome tests/
```
Target coverage: 75–100%

## ⚙️ Environment Configuration
ScrapeSome reads from environment variables if a .env file is present.

Example .env

```env
LOG_LEVEL=INFO
EXPORT_FORMAT=text
FETCH_PLAYWRIGHT_TIMEOUT=10
FETCH_PAGE_TIMEOUT=10
```

| Variable                 | Description                                          |
|--------------------------|------------------------------------------------------|
| FETCH_PLAYWRIGHT_TIMEOUT | Timeout for Playwright-rendered pages (in seconds)  |
| FETCH_PAGE_TIMEOUT       | Timeout for standard page fetch (in seconds)        |
| LOG_LEVEL                | Logging verbosity (DEBUG, INFO, WARNING, etc.)      |
| EXPORT_FORMAT            | Default export format (text, markdown, json, html)  |

## 📄 Output Formats

JSON Example

Get `json` version

```python
from scrapesome.scraper.sync_scraper import scraper
content = scraper("https://example.com", format_type="json")
content
```

Output

```json
{
  "title": "Example Domain",
  "description": "This domain is for use in illustrative examples.",
  "url": "https://example.com"
}
```

## Markdown

Convert HTML to Markdown with:

```python
from scrapesome.scraper.sync_scraper import scraper
content = scraper("https://adenuniversity.us", format_type="markdown")
content
```
Output

```text
# Online Global Masters that boost your global career

**ADEN University** offers students access to professionals who operate in the world of business and administration, who share their knowledge and acumen collaboratively with their students in all **academic programs** offered at ADEN.

[About Us](about-aden-university)


Watch testimonial video 


##### Watch testimonial video

×

[

](https://res.cloudinary.com/cruminott/video/upload/vc_auto,w_auto,q_auto,f_auto/adenu/aden-university-3.mp4)



## ADEN University offers the following academic programs

[![EXECUTIVE MBA. Master of Business Administration](https://adenuniversity.us/files/2016/06/ADENU_miniatura_Emba_900-1-820x400.jpg "EXECUTIVE MBA. Master of Business Administration")](https://adenuniversity.us/academics/executive-mba/  "EXECUTIVE MBA. Master of Business Administration")

##### [EXECUTIVE MBA. Master of Business Administration](https://adenuniversity.us/academics/executive-mba/ "EXECUTIVE MBA. Master of Business Administration")

The ADEN University Executive MBA is designed to strengthen business leaders to manage...

* **37** credits
* **15** months
* **Spanish Only**

[Visit EMBA Course](https://adenuniversity.us/academics/executive-mba/ "EXECUTIVE MBA. Master of Business Administration")

[![GLOBAL MBA. Master of Business Administration](https://adenuniversity.us/files/2016/06/ADENU_miniatura_MBAgl1_900-820x400.jpg "GLOBAL MBA. Master of Business Administration")](https://adenuniversity.us/academics/global-mba/  "GLOBAL MBA. Master of Business Administration")

##### [GLOBAL MBA. Master of Business Administration](https://adenuniversity.us/academics/global-mba/ "GLOBAL MBA. Master of Business Administration")

The Global MBA is designed to prepare business leaders to manage companies in an...

* **36** credits
* **14** months
* **Spanish and English**
```

Similarly async can also be used.

## 📁 Project Structure

```text
scrapesome/
├── config.py
├── exceptions.py
├── formatter/
│   └── output_formatter.py
├── logging.py
├── scraper/
│   ├── async_scraper.py
│   ├── sync_scraper.py
│   └── rendering.py
```

## 🔒 License
MIT License © 2025

## 🧑‍💻 Author
Crafted with care by `Vishnu Vardhan Reddy`
Contributions welcome! 🙌
