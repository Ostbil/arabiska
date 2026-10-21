const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ });
  for (const s of process.argv.slice(2)) {
    const p = await b.newPage();
    p.on('pageerror', e => console.log('ERR', e.message));
    await p.goto('file://' + process.cwd() + '/print_' + s + '.html');
    await p.waitForSelector('body[data-ready]', { timeout: 60000 });
    await p.pdf({ path: 'print_' + s + '.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
    await p.screenshot({ path: 'print_' + s + '.png', clip: { x: 0, y: 0, width: 794, height: 2246 } });
  }
  await b.close();
})();
