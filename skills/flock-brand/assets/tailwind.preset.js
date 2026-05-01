/**
 * FLock.io Brand — Tailwind preset
 *
 * Usage:
 *   // tailwind.config.js
 *   const flock = require('./flock-brand/assets/tailwind.preset.js');
 *   module.exports = { presets: [flock], content: [...] };
 *
 * Token authority: PDF-canonical (Section 1) + internal extensions (Section 2).
 * See ../references/colors.md for what's official vs extended.
 */

module.exports = {
  theme: {
    extend: {
      colors: {
        flock: {
          // Primary (PDF-canonical)
          blue:        '#3773FF',
          black:       '#000000',
          'off-white': '#F2F2F2',
          white:       '#FFFFFF',
          // Secondary (PDF-canonical, accents only)
          orange:      '#FF8B00',
          turquoise:   '#03BFD4',
          purple:      '#9C59F3',
          // Extended
          green:       '#22B473',
          border:      '#E0E4F0',
          surface:     '#F8F8F8',
          // Pillar tints
          'tint-blue':   '#98B8F8',
          'tint-teal':   '#B8E8F0',
          'tint-purple': '#D0B8F8',
          'tint-orange': '#F8D0A8',
        },
      },
      fontFamily: {
        flock: [
          'TWK Everett', 'Inter', 'SF Pro Display',
          'Alibaba PuHuiTi 3.0',
          'PingFang SC', 'Hiragino Sans GB', 'Noto Sans SC', 'Source Han Sans SC',
          'Microsoft YaHei',
          'Helvetica Neue', 'Arial', 'sans-serif',
        ],
        mono: ['SF Mono', 'JetBrains Mono', 'Fira Code', 'Consolas', 'monospace'],
      },
      fontSize: {
        // PDF-canonical type scale
        'flock-h1':      ['64px', { lineHeight: '1.0', letterSpacing: '-0.04em', fontWeight: '700' }],
        'flock-h2':      ['48px', { lineHeight: '1.0', letterSpacing: '-0.04em', fontWeight: '500' }],
        'flock-h3':      ['36px', { lineHeight: '1.2', letterSpacing: '-0.03em', fontWeight: '500' }],
        'flock-body':    ['24px', { lineHeight: '1.2', letterSpacing: '-0.03em', fontWeight: '400' }],
        // Extended
        'flock-caption': ['14px', { lineHeight: '1.4', fontWeight: '400' }],
        'flock-data':    ['12px', { lineHeight: '1.4', fontWeight: '400' }],
      },
      letterSpacing: {
        'flock-tight':  '-0.04em',
        'flock-normal': '-0.03em',
        'flock-cjk':    '-0.01em',
      },
      borderRadius: {
        'flock-sm': '4px',
        'flock-md': '8px',
        'flock-lg': '12px',
        'flock-xl': '16px',
      },
      spacing: {
        'flock-xs':  '4px',
        'flock-sm':  '8px',
        'flock-md':  '16px',
        'flock-lg':  '24px',
        'flock-xl':  '32px',
        'flock-2xl': '48px',
        'flock-3xl': '64px',
      },
    },
  },
};
