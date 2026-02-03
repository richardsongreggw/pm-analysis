#!/usr/bin/env python3
"""
Generate landscape PDF from HTML slides
Uses Playwright to render and print the reveal.js slides to PDF
"""

import os
import sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Error: playwright not installed")
    print("Installing playwright...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
    from playwright.sync_api import sync_playwright

def generate_slides_pdf():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)

    # Input HTML file
    html_file = os.path.join(project_dir, "presentations", "sibling_feature_business_case_slides.html")
    html_path = f"file://{html_file}"

    # Output PDF file
    output_file = os.path.join(project_dir, "presentations", "sibling_feature_business_case_slides.pdf")

    if not os.path.exists(html_file):
        print(f"Error: HTML file not found at {html_file}")
        return

    print(f"Converting slides to PDF...")
    print(f"Input: {html_file}")
    print(f"Output: {output_file}")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate to the HTML file
        page.goto(html_path)

        # Wait for reveal.js to initialize
        page.wait_for_timeout(2000)

        # Get total number of slides
        total_slides = page.evaluate("""() => {
            return Reveal.getTotalSlides();
        }""")

        print(f"Found {total_slides} slides")

        # Print to PDF with landscape orientation
        # Size: 1680x946 (as per slides)
        page.pdf(
            path=output_file,
            format='Letter',  # 11 x 8.5 inches
            landscape=True,
            print_background=True,
            margin={
                'top': '0.2in',
                'right': '0.2in',
                'bottom': '0.2in',
                'left': '0.2in'
            },
            prefer_css_page_size=False
        )

        browser.close()

    print(f"\n✅ PDF generated successfully!")
    print(f"Location: {output_file}")

    # Check file size
    file_size = os.path.getsize(output_file) / (1024 * 1024)  # MB
    print(f"File size: {file_size:.1f} MB")

if __name__ == "__main__":
    generate_slides_pdf()
