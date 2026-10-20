import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        await pg.goto('file://' + __import__('os').path.abspath('brochure.html') + '')
        await pg.wait_for_load_state('networkidle')
        await pg.evaluate('document.fonts.ready')
        await pg.pdf(path='../Tezoro_Brand_Proposal_DARTS_AI.pdf', format='A4', print_background=True, margin={'top':'0','right':'0','bottom':'0','left':'0'}, prefer_css_page_size=True)
        await b.close()
asyncio.run(main())
