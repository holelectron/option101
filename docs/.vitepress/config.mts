import { defineConfig } from 'vitepress'
import { readFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { dirname, resolve } from 'node:path'
import './theme/custom.css'

const here = dirname(fileURLToPath(import.meta.url))
const manifest = JSON.parse(readFileSync(resolve(here, '../skylit/manifest.json'), 'utf8'))
const sections: Record<string, [string, string]> = {
  academy: ['Skylit Academy', '시장 구조 · 학습'],
  greeks: ['The Greeks', '그릭스 · 민감도'],
  heatseeker: ['Heatseeker', 'GEX · VEX'],
  flowseeker: ['Flowseeker', '옵션 플로우'],
  tools: ['Tools & Comparisons', '도구와 비교']
}

function sidebar(korean: boolean) {
  return Object.entries(sections).map(([id, names]) => ({
    text: korean ? names[1] : names[0],
    collapsed: false,
    items: manifest.articles.filter((a: any) => a.category === id).map((a: any) => {
      const p = a.markdown.replace(/^docs\//, '').replace(/\.md$/, '')
      return { text: a.title, link: '/' + (korean ? 'ko/' : '') + p }
    })
  }))
}

export default defineConfig({
  title: 'option101',
  description: 'Options trading research & Skylit knowledge hub',
  base: '/option101/',
  cleanUrls: true,
  srcExclude: ['skylit/**/*.ko.md', 'skylit/**/*.html', 'skylit/_landing.html'],
  sitemap: { hostname: 'https://holelectron.github.io/option101/' },
  head: [['meta', { name: 'theme-color', content: '#101a2c' }]],
  locales: {
    root: {
      label: 'English',
      lang: 'en-US',
      themeConfig: {
        nav: [
          { text: 'Home', link: '/' },
          { text: 'All documents', link: '/skylit/INDEX' },
          { text: '한국어', link: '/ko/' }
        ],
        sidebar: sidebar(false),
        outline: { label: 'On this page' },
        docFooter: { prev: 'Previous', next: 'Next' },
        lastUpdated: { text: 'Updated' }
      }
    },
    ko: {
      label: '한국어',
      lang: 'ko-KR',
      link: '/ko/',
      themeConfig: {
        nav: [
          { text: '홈', link: '/ko/' },
          { text: '전체 문서', link: '/ko/skylit/' },
          { text: 'English', link: '/' }
        ],
        sidebar: sidebar(true),
        outline: { label: '이 페이지에서' },
        docFooter: { prev: '이전', next: '다음' },
        lastUpdated: { text: '수정' }
      }
    }
  },
  themeConfig: {
    logo: undefined,
    siteTitle: 'option101',
    search: { provider: 'local' },
    socialLinks: [{ icon: 'github', link: 'https://github.com/holelectron/option101' }],
    footer: { message: 'Personal research archive · Not investment advice', copyright: 'option101' }
  },
  markdown: { theme: { light: 'github-light', dark: 'github-dark' }, lineNumbers: true }
})
