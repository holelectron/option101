import fs from 'node:fs'
import path from 'node:path'

const root = process.cwd()
const source = path.join(root, 'docs', 'skylit')
const destination = path.join(root, 'docs', 'ko', 'skylit')
const manifest = JSON.parse(fs.readFileSync(path.join(source, 'manifest.json'), 'utf-8'))

for (const a of manifest.articles) {
  const englishPath = path.join(root, a.markdown)
  const relative = path.relative(source, englishPath)
  const output = path.join(destination, relative)
  const translatedPath = englishPath.replace(/\.md$/, '.ko.md')
  fs.mkdirSync(path.dirname(output), { recursive: true })
  const hasTranslation = fs.existsSync(translatedPath)
  if (hasTranslation) {
    // The original and generated files stay separate: originals remain intact.
    const text = fs.readFileSync(translatedPath, 'utf-8')
    fs.writeFileSync(output, text)
  } else {
    fs.writeFileSync(output, `# ${a.title}\n\n> 한국어 번역이 준비 중입니다. 현재 [영어 원문](/skylit/${relative.replace(/\\/g, '/').replace(/\.md$/, '')})을 읽을 수 있습니다.\n\n[원본 사이트](${a.url})\n`)
  }
}
const index = [
  '# 한국어 문서 목차',
  '',
  '번역 파일이 없는 문서는 영어 원문으로 연결됩니다.',
  ''
]
for (const category of [...new Set(manifest.articles.map(a => a.category))]) {
  index.push('## ' + category, '')
  for (const a of manifest.articles.filter(a => a.category === category)) {
    const route = a.markdown.replace(/^docs\//, '').replace(/\.md$/, '')
    index.push(`- [${a.title}](/ko/${route}) · [영어](/${route})`)
  }
  index.push('')
}
fs.writeFileSync(path.join(destination, 'index.md'), index.join('\n'))
console.log(`Prepared ${manifest.articles.length} Korean site routes.`)
